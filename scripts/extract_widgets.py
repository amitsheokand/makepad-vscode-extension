#!/usr/bin/env python3
"""
Extract widget definitions from Makepad source code to generate VS Code snippets.
This script parses the Makepad widgets source to create:
1. Widget snippets with their properties
2. Property value completions
3. Documentation for hover tooltips
"""

import os
import re
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# Default path - override with MAKEPAD_PATH environment variable
MAKEPAD_WIDGETS_PATH = Path(os.environ.get("MAKEPAD_PATH", "")).joinpath("widgets/src") if os.environ.get("MAKEPAD_PATH") else Path.home() / "makepad" / "widgets" / "src"

@dataclass
class WidgetProperty:
    name: str
    prop_type: str
    default: Optional[str] = None
    doc: str = ""

@dataclass 
class Widget:
    name: str
    file: str
    properties: list = field(default_factory=list)
    doc: str = ""
    is_usable: bool = True  # Some are internal/Draw* types

def extract_widgets():
    """Extract all widget definitions from Makepad source."""
    widgets = {}
    
    for rs_file in MAKEPAD_WIDGETS_PATH.glob("*.rs"):
        content = rs_file.read_text()
        
        # Find structs with #[derive(...Live...Widget...)]
        # Pattern: #[derive(...)] ... pub struct Name { ... }
        struct_pattern = r'#\[derive\([^\]]*(?:Live|Widget)[^\]]*\)\]\s*(?:#\[[^\]]*\]\s*)*pub struct (\w+)\s*\{'
        
        for match in re.finditer(struct_pattern, content):
            name = match.group(1)
            
            # Skip internal types
            if name.startswith('Draw') or name.endswith('Ref') or name.endswith('Set'):
                continue
            if name in ['WidgetAction', 'WidgetActionData', 'WidgetUid', 'WidgetRegistry']:
                continue
                
            # Extract properties
            struct_start = match.end()
            brace_count = 1
            struct_end = struct_start
            
            for i, char in enumerate(content[struct_start:]):
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        struct_end = struct_start + i
                        break
            
            struct_body = content[struct_start:struct_end]
            properties = extract_properties(struct_body)
            
            # Get doc comment
            doc = extract_doc_comment(content, match.start())
            
            widgets[name] = Widget(
                name=name,
                file=rs_file.name,
                properties=properties,
                doc=doc
            )
    
    return widgets

def extract_properties(struct_body: str) -> list:
    """Extract #[live] properties from struct body."""
    properties = []
    
    # Pattern for #[live] or #[live(default)] followed by field: Type
    live_pattern = r'#\[live(?:\(([^)]*)\))?\]\s*(?:pub\s+)?(\w+):\s*([^,\n]+)'
    
    for match in re.finditer(live_pattern, struct_body):
        default = match.group(1)
        name = match.group(2)
        prop_type = match.group(3).strip().rstrip(',')
        
        properties.append(WidgetProperty(
            name=name,
            prop_type=prop_type,
            default=default
        ))
    
    return properties

def extract_doc_comment(content: str, pos: int) -> str:
    """Extract /// doc comments before a struct."""
    lines = content[:pos].split('\n')
    doc_lines = []
    
    for line in reversed(lines[-10:]):
        stripped = line.strip()
        if stripped.startswith('///'):
            doc_lines.insert(0, stripped[3:].strip())
        elif stripped and not stripped.startswith('#'):
            break
    
    return ' '.join(doc_lines)

def generate_snippets(widgets: dict) -> dict:
    """Generate VS Code snippets from widgets."""
    snippets = {}
    
    # Common widgets that should have detailed snippets
    common_widgets = [
        'View', 'Button', 'Label', 'Image', 'TextInput', 'CheckBox', 
        'Slider', 'DropDown', 'ScrollBars', 'PortalList', 'Window',
        'Root', 'RadioButton', 'FoldButton', 'Icon', 'Html', 'Markdown',
        'Video', 'Splitter', 'TabBar', 'StackNavigation', 'Modal',
        'Tooltip', 'ExpandablePanel', 'ColorPicker', 'FileTree'
    ]
    
    for name, widget in widgets.items():
        if name in common_widgets:
            snippet = generate_widget_snippet(widget)
            snippets[f"{name} Widget"] = snippet
    
    return snippets

def generate_widget_snippet(widget: Widget) -> dict:
    """Generate a single widget snippet."""
    prefix = f"mp{widget.name.lower()}"
    
    # Build body
    body_lines = [f"${{1:{widget.name.lower()}_name}} = <{widget.name}> {{"]
    
    # Add common properties based on widget type
    if widget.name == 'View':
        body_lines.extend([
            "    width: ${2|Fill,Fit,100|}",
            "    height: ${3|Fill,Fit,100|}",
            "    flow: ${4|Down,Right,Overlay,RightWrap|}",
            "    $0"
        ])
    elif widget.name == 'Button':
        body_lines.extend([
            '    text: "${2:Button Text}"',
            "    $0"
        ])
    elif widget.name == 'Label':
        body_lines.extend([
            '    text: "${2:Label Text}"',
            "    draw_text: {",
            "        color: ${3:#fff}",
            "        text_style: {font_size: ${4:14.0}}",
            "    }",
            "    $0"
        ])
    elif widget.name == 'Image':
        body_lines.extend([
            "    width: ${2|Fill,Fit,100|}",
            "    height: ${3|Fill,Fit,100|}",
            "    fit: ${4|Centered,Smallest,Biggest,Stretch,Size|}",
            "    $0"
        ])
    elif widget.name == 'TextInput':
        body_lines.extend([
            "    width: ${2:200.0}",
            '    empty_text: "${3:Enter text...}"',
            "    $0"
        ])
    elif widget.name == 'CheckBox':
        body_lines.extend([
            '    text: "${2:Checkbox Label}"',
            "    $0"
        ])
    elif widget.name == 'Slider':
        body_lines.extend([
            "    width: ${2:150.0}",
            "    min: ${3:0.0}",
            "    max: ${4:100.0}",
            "    step: ${5:1.0}",
            "    $0"
        ])
    elif widget.name == 'PortalList':
        body_lines.extend([
            "    flow: ${2|Down,Right|}",
            "    spacing: ${3:5}",
            "    ${4:item_template} = <View> {",
            "        width: ${5|Fill,100|}",
            "        height: ${6|Fit,100|}",
            "        $0",
            "    }"
        ])
    else:
        body_lines.append("    $0")
    
    body_lines.append("}")
    
    description = widget.doc if widget.doc else f"Makepad {widget.name} widget"
    
    return {
        "prefix": prefix,
        "body": body_lines,
        "description": description
    }

def generate_property_snippets() -> dict:
    """Generate snippets for common properties."""
    return {
        "Width Fill": {"prefix": "wfill", "body": "width: Fill", "description": "width: Fill"},
        "Width Fit": {"prefix": "wfit", "body": "width: Fit", "description": "width: Fit"},
        "Width Fixed": {"prefix": "wfixed", "body": "width: ${1:100}", "description": "width: fixed value"},
        "Height Fill": {"prefix": "hfill", "body": "height: Fill", "description": "height: Fill"},
        "Height Fit": {"prefix": "hfit", "body": "height: Fit", "description": "height: Fit"},
        "Height Fixed": {"prefix": "hfixed", "body": "height: ${1:100}", "description": "height: fixed value"},
        "Flow Down": {"prefix": "flowdown", "body": "flow: Down", "description": "flow: Down"},
        "Flow Right": {"prefix": "flowright", "body": "flow: Right", "description": "flow: Right"},
        "Flow Overlay": {"prefix": "flowoverlay", "body": "flow: Overlay", "description": "flow: Overlay"},
        "Flow RightWrap": {"prefix": "flowrightwrap", "body": "flow: RightWrap", "description": "flow: RightWrap"},
        "Align Center": {"prefix": "aligncenter", "body": "align: {x: 0.5, y: 0.5}", "description": "Center alignment"},
        "Align Top Left": {"prefix": "aligntl", "body": "align: {x: 0.0, y: 0.0}", "description": "Top-left alignment"},
        "Align Top Right": {"prefix": "aligntr", "body": "align: {x: 1.0, y: 0.0}", "description": "Top-right alignment"},
        "Align Bottom Left": {"prefix": "alignbl", "body": "align: {x: 0.0, y: 1.0}", "description": "Bottom-left alignment"},
        "Align Bottom Right": {"prefix": "alignbr", "body": "align: {x: 1.0, y: 1.0}", "description": "Bottom-right alignment"},
        "Padding All": {"prefix": "mppadding", "body": "padding: ${1:10}", "description": "Padding (all sides)"},
        "Padding Sides": {"prefix": "mppaddingsides", "body": "padding: {top: ${1:10}, right: ${2:10}, bottom: ${3:10}, left: ${4:10}}", "description": "Padding (individual sides)"},
        "Margin All": {"prefix": "mpmargin", "body": "margin: ${1:10}", "description": "Margin (all sides)"},
        "Margin Sides": {"prefix": "mpmarginsides", "body": "margin: {top: ${1:10}, right: ${2:10}, bottom: ${3:10}, left: ${4:10}}", "description": "Margin (individual sides)"},
        "Spacing": {"prefix": "mpspacing", "body": "spacing: ${1:5}", "description": "Spacing between children"},
        "Show Background": {"prefix": "mpshowbg", "body": ["show_bg: true", "draw_bg: {", "    color: ${1:#333}", "}"], "description": "Show background with color"},
        "Background Shader": {"prefix": "mpdrawbg", "body": ["draw_bg: {", "    fn pixel(self) -> vec4 {", "        return ${1:#333};", "    }", "}"], "description": "Custom background shader"},
        "Cursor Pointer": {"prefix": "mpcursor", "body": "cursor: ${1|Hand,Arrow,Text,Move,Wait,Help,NotAllowed|}", "description": "Mouse cursor style"},
    }

def generate_rust_snippets() -> dict:
    """Generate snippets for Rust code patterns."""
    return {
        "Live Design Block": {
            "prefix": "live_design",
            "body": [
                "live_design!(",
                "    use link::widgets::*;",
                "    use link::theme::*;",
                "    use link::shaders::*;",
                "",
                "    pub ${1:WidgetName} = {{${1:WidgetName}}} {",
                "        $0",
                "    }",
                ");"
            ],
            "description": "Create a live_design! block"
        },
        "Widget Struct": {
            "prefix": "mpwidgetstruct",
            "body": [
                "#[derive(Live, LiveHook, Widget)]",
                "pub struct ${1:WidgetName} {",
                "    #[deref]",
                "    deref: ${2:View},",
                "    #[rust]",
                "    ${3:state}: ${4:State},",
                "}"
            ],
            "description": "Makepad Widget struct definition"
        },
        "Widget Impl": {
            "prefix": "mpwidgetimpl",
            "body": [
                "impl Widget for ${1:WidgetName} {",
                "    fn handle_event(&mut self, cx: &mut Cx, event: &Event, scope: &mut Scope) {",
                "        self.deref.handle_event(cx, event, scope);",
                "        self.widget_match_event(cx, event, scope);",
                "    }",
                "",
                "    fn draw_walk(&mut self, cx: &mut Cx2d, scope: &mut Scope, walk: Walk) -> DrawStep {",
                "        self.deref.draw_walk(cx, scope, walk)",
                "    }",
                "}"
            ],
            "description": "Widget trait implementation"
        },
        "WidgetMatchEvent Impl": {
            "prefix": "mpwidgetmatch",
            "body": [
                "impl WidgetMatchEvent for ${1:WidgetName} {",
                "    fn handle_actions(&mut self, cx: &mut Cx, actions: &Actions, scope: &mut Scope) {",
                "        $0",
                "    }",
                "}"
            ],
            "description": "WidgetMatchEvent implementation"
        },
        "MatchEvent Impl": {
            "prefix": "mpmatchevent",
            "body": [
                "impl MatchEvent for ${1:App} {",
                "    fn handle_startup(&mut self, cx: &mut Cx) {",
                "        $0",
                "    }",
                "",
                "    fn handle_shutdown(&mut self, _cx: &mut Cx) {}",
                "}"
            ],
            "description": "MatchEvent implementation for App"
        },
        "AppMain Impl": {
            "prefix": "mpappmain",
            "body": [
                "impl AppMain for ${1:App} {",
                "    fn handle_event(&mut self, cx: &mut Cx, event: &Event) {",
                "        self.ui.handle_event(cx, event, &mut Scope::empty());",
                "        self.match_event(cx, event);",
                "    }",
                "}"
            ],
            "description": "AppMain implementation"
        },
        "LiveRegister Impl": {
            "prefix": "mpliveregister",
            "body": [
                "impl LiveRegister for ${1:App} {",
                "    fn live_register(cx: &mut Cx) {",
                "        makepad_widgets::live_design(cx);",
                "        crate::${2:ui}::live_design(cx);",
                "    }",
                "}"
            ],
            "description": "LiveRegister implementation"
        },
        "Button Click Handler": {
            "prefix": "mpbtnclick",
            "body": [
                "if self.${1:ui}.${2:button}(id!(${3:btn_name})).clicked(actions) {",
                "    $0",
                "}"
            ],
            "description": "Button click handler"
        },
        "Keyboard Event Handler": {
            "prefix": "mpkeydown",
            "body": [
                "match event.hits(cx, self.${1:deref}.area()) {",
                "    Hit::KeyDown(KeyEvent { key_code: KeyCode::${2:ArrowRight}, .. }) => {",
                "        $0",
                "    }",
                "    _ => {}",
                "}"
            ],
            "description": "Keyboard event handler"
        },
        "Finger Down Handler": {
            "prefix": "mpfingerdown",
            "body": [
                "match event.hits(cx, ${1:widget}.area()) {",
                "    Hit::FingerDown(_) => {",
                "        $0",
                "    }",
                "    _ => {}",
                "}"
            ],
            "description": "Finger/mouse down handler"
        },
        "Redraw": {
            "prefix": "mpredraw",
            "body": "self.${1:ui}.redraw(cx);",
            "description": "Redraw the UI"
        },
        "App Main Macro": {
            "prefix": "app_main",
            "body": "app_main!(${1:App});",
            "description": "app_main! macro call"
        },
        "Root Window": {
            "prefix": "mproot",
            "body": [
                "<Root> {",
                "    main_window = <Window> {",
                "        window: {inner_size: vec2(${1:800}, ${2:600})}",
                "        body = <View> {",
                "            width: Fill",
                "            height: Fill",
                "            $0",
                "        }",
                "    }",
                "}"
            ],
            "description": "Root with Window"
        },
        "Animator Block": {
            "prefix": "mpanimator",
            "body": [
                "animator: {",
                "    ${1:hover} = {",
                "        default: off",
                "        off = {",
                "            from: {all: Forward {duration: ${2:0.2}}}",
                "            apply: {",
                "                draw_bg: {color: ${3:#333}}",
                "            }",
                "        }",
                "        on = {",
                "            from: {all: Forward {duration: ${2:0.2}}}",
                "            apply: {",
                "                draw_bg: {color: ${4:#555}}",
                "            }",
                "        }",
                "    }",
                "}"
            ],
            "description": "Animator with on/off states"
        },
        "Image Load Async": {
            "prefix": "mpimgload",
            "body": [
                "let img = self.${1:ui}.image(id!(${2:image_name}));",
                "img.load_image_file_by_path_async(cx, &${3:path});"
            ],
            "description": "Load image asynchronously"
        },
        "PortalList Draw": {
            "prefix": "mpportallistdraw",
            "body": [
                "let list = self.${1:ui}.portal_list(id!(${2:list_name}));",
                "while let Some(index) = list.next_visible_item(cx) {",
                "    let item = list.item(cx, index, live_id!(${3:item_template}));",
                "    $0",
                "    item.draw_all(cx, scope);",
                "}"
            ],
            "description": "PortalList drawing pattern"
        }
    }

def generate_layout_snippets() -> dict:
    """Generate snippets for common layout patterns."""
    return {
        "Horizontal Layout": {
            "prefix": "mplayouth",
            "body": [
                "<View> {",
                "    width: Fill",
                "    height: Fit",
                "    flow: Right",
                "    spacing: ${1:10}",
                "    align: {y: 0.5}",
                "    $0",
                "}"
            ],
            "description": "Horizontal layout (row)"
        },
        "Vertical Layout": {
            "prefix": "mplayoutv",
            "body": [
                "<View> {",
                "    width: Fill",
                "    height: Fill",
                "    flow: Down",
                "    spacing: ${1:10}",
                "    $0",
                "}"
            ],
            "description": "Vertical layout (column)"
        },
        "Centered Container": {
            "prefix": "mpcenter",
            "body": [
                "<View> {",
                "    width: Fill",
                "    height: Fill",
                "    align: {x: 0.5, y: 0.5}",
                "    $0",
                "}"
            ],
            "description": "Centered container"
        },
        "ScrollX View": {
            "prefix": "mpscrollx",
            "body": [
                "<ScrollXView> {",
                "    width: Fill",
                "    height: ${1:100}",
                "    flow: Right",
                "    spacing: ${2:5}",
                "    $0",
                "}"
            ],
            "description": "Horizontal scrollable view"
        },
        "ScrollY View": {
            "prefix": "mpscrolly",
            "body": [
                "<ScrollYView> {",
                "    width: Fill",
                "    height: Fill",
                "    flow: Down",
                "    spacing: ${1:5}",
                "    $0",
                "}"
            ],
            "description": "Vertical scrollable view"
        },
        "Filler": {
            "prefix": "mpfiller",
            "body": "<Filler> {}",
            "description": "Flexible space filler"
        },
        "Hr": {
            "prefix": "mphr",
            "body": "<Hr> {}",
            "description": "Horizontal rule"
        },
        "Vr": {
            "prefix": "mpvr", 
            "body": "<Vr> {}",
            "description": "Vertical rule"
        }
    }

def main():
    print("Extracting widgets from Makepad source...")
    widgets = extract_widgets()
    print(f"Found {len(widgets)} widgets")
    
    # Generate all snippets
    all_snippets = {}
    
    # Widget snippets
    widget_snippets = generate_snippets(widgets)
    all_snippets.update(widget_snippets)
    print(f"Generated {len(widget_snippets)} widget snippets")
    
    # Property snippets
    prop_snippets = generate_property_snippets()
    all_snippets.update(prop_snippets)
    print(f"Generated {len(prop_snippets)} property snippets")
    
    # Rust code snippets
    rust_snippets = generate_rust_snippets()
    all_snippets.update(rust_snippets)
    print(f"Generated {len(rust_snippets)} Rust code snippets")
    
    # Layout snippets
    layout_snippets = generate_layout_snippets()
    all_snippets.update(layout_snippets)
    print(f"Generated {len(layout_snippets)} layout snippets")
    
    print(f"\nTotal: {len(all_snippets)} snippets")
    
    # Write to file
    output_path = Path(__file__).parent.parent / "snippets" / "makepad.json"
    with open(output_path, 'w') as f:
        json.dump(all_snippets, f, indent=2)
    
    print(f"Written to {output_path}")
    
    # Also generate documentation
    generate_documentation(widgets)

def generate_documentation(widgets: dict):
    """Generate markdown documentation for widgets."""
    doc_path = Path(__file__).parent.parent / "docs" / "WIDGETS.md"
    doc_path.parent.mkdir(exist_ok=True)
    
    with open(doc_path, 'w') as f:
        f.write("# Makepad Widgets Reference\n\n")
        f.write("Auto-generated from Makepad source code.\n\n")
        f.write("## Table of Contents\n\n")
        
        for name in sorted(widgets.keys()):
            f.write(f"- [{name}](#{name.lower()})\n")
        
        f.write("\n---\n\n")
        
        for name, widget in sorted(widgets.items()):
            f.write(f"## {name}\n\n")
            f.write(f"**File:** `{widget.file}`\n\n")
            
            if widget.doc:
                f.write(f"{widget.doc}\n\n")
            
            if widget.properties:
                f.write("### Properties\n\n")
                f.write("| Property | Type | Default |\n")
                f.write("|----------|------|--------|\n")
                for prop in widget.properties:
                    default = prop.default if prop.default else "-"
                    f.write(f"| `{prop.name}` | `{prop.prop_type}` | {default} |\n")
                f.write("\n")
            
            f.write("### Example\n\n")
            f.write("```rust\n")
            f.write(f"my_{name.lower()} = <{name}> {{\n")
            f.write("    // properties here\n")
            f.write("}\n")
            f.write("```\n\n")
            f.write("---\n\n")
    
    print(f"Documentation written to {doc_path}")

if __name__ == "__main__":
    main()

