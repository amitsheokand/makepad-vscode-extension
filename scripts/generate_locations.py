#!/usr/bin/env python3
"""
Generate widget and property locations for Go-to-Definition support.
"""

import os
import re
import json
from pathlib import Path

# Default path - override with MAKEPAD_PATH environment variable
MAKEPAD_WIDGETS_PATH = Path(os.environ.get("MAKEPAD_PATH", "")).joinpath("widgets/src") if os.environ.get("MAKEPAD_PATH") else Path.home() / "makepad" / "widgets" / "src"

def find_widget_locations():
    """Find all widget struct definitions and their locations."""
    locations = {}
    
    for rs_file in MAKEPAD_WIDGETS_PATH.glob("*.rs"):
        content = rs_file.read_text()
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Match: pub struct WidgetName {
            match = re.match(r'^pub struct (\w+)\s*\{', line)
            if match:
                name = match.group(1)
                # Skip internal types
                if name.endswith('Ref') or name.endswith('Set') or name.startswith('Draw'):
                    continue
                if name in ['WidgetAction', 'WidgetActionData', 'WidgetUid', 'WidgetRegistry']:
                    continue
                    
                locations[name] = {
                    'file': str(rs_file),
                    'line': i + 1  # 1-indexed
                }
    
    return locations

def find_property_locations():
    """Find common property definitions."""
    # Properties are typically defined in draw.rs or walk types
    # For simplicity, we'll point to the View struct which has most properties
    view_file = MAKEPAD_WIDGETS_PATH / "view.rs"
    
    properties = {}
    content = view_file.read_text()
    lines = content.split('\n')
    
    # Find #[live] properties
    for i, line in enumerate(lines):
        match = re.search(r'#\[live.*?\]\s*(?:pub\s+)?(\w+):', line)
        if match:
            prop_name = match.group(1)
            properties[prop_name] = {
                'file': str(view_file),
                'line': i + 1
            }
    
    # Add Walk properties (width, height, margin, etc.) from draw crate
    makepad_root = Path(os.environ.get("MAKEPAD_PATH", "")) if os.environ.get("MAKEPAD_PATH") else Path.home() / "makepad"
    walk_file = makepad_root / "draw" / "src" / "cx_2d.rs"
    if walk_file.exists():
        content = walk_file.read_text()
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'pub struct Walk' in line:
                # Point width/height to Walk definition
                properties['width'] = {'file': str(walk_file), 'line': i + 1}
                properties['height'] = {'file': str(walk_file), 'line': i + 1}
                break
    
    return properties

def main():
    print("Finding widget locations...")
    widgets = find_widget_locations()
    print(f"Found {len(widgets)} widgets")
    
    print("Finding property locations...")
    properties = find_property_locations()
    print(f"Found {len(properties)} properties")
    
    # Output as TypeScript
    output = {
        'widgets': widgets,
        'properties': properties
    }
    
    output_path = Path(__file__).parent.parent / "src" / "locations.json"
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"Written to {output_path}")
    
    # Also output stats
    print("\nSample widgets:")
    for name in list(widgets.keys())[:10]:
        loc = widgets[name]
        print(f"  {name}: {loc['file']}:{loc['line']}")

if __name__ == "__main__":
    main()

