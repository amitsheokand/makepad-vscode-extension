import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';

// Makepad widgets source path - discovered dynamically
let MAKEPAD_WIDGETS_PATH: string | null = null;

// Widget locations (populated at activation)
let WIDGET_LOCATIONS: Record<string, { file: string; line: number }> = {};
let PROPERTY_LOCATIONS: Record<string, { file: string; line: number }> = {};

// Widget documentation
const WIDGET_DOCS: Record<string, { description: string; properties: string[]; example: string }> = {
    'View': {
        description: 'The fundamental container widget. Holds other widgets and controls layout.',
        properties: ['width', 'height', 'flow', 'spacing', 'padding', 'margin', 'align', 'show_bg', 'draw_bg'],
        example: `<View> {\n    width: Fill\n    height: Fill\n    flow: Down\n    spacing: 10\n}`
    },
    'Button': {
        description: 'Interactive button widget with customizable appearance and click handling.',
        properties: ['text', 'draw_bg', 'draw_text', 'draw_icon'],
        example: `my_button = <Button> {\n    text: "Click Me"\n}`
    },
    'Label': {
        description: 'Text display widget with styling options.',
        properties: ['text', 'draw_text'],
        example: `my_label = <Label> {\n    text: "Hello World"\n}`
    },
    'Image': {
        description: 'Image display widget supporting various fit modes and async loading.',
        properties: ['source', 'fit', 'width', 'height'],
        example: `my_image = <Image> {\n    width: Fill\n    height: Fill\n    fit: Centered\n}`
    },
    'TextInput': {
        description: 'Single-line text input field.',
        properties: ['text', 'empty_text', 'is_read_only'],
        example: `my_input = <TextInput> {\n    width: 200.0\n    empty_text: "Enter text..."\n}`
    },
    'CheckBox': {
        description: 'Toggle checkbox with optional label.',
        properties: ['text', 'is_checked'],
        example: `my_checkbox = <CheckBox> {\n    text: "Enable feature"\n}`
    },
    'Slider': {
        description: 'Horizontal slider for numeric input.',
        properties: ['min', 'max', 'step', 'default'],
        example: `my_slider = <Slider> {\n    width: 150.0\n    min: 0.0\n    max: 100.0\n}`
    },
    'PortalList': {
        description: 'Virtualized list for efficiently rendering large datasets.',
        properties: ['flow', 'spacing'],
        example: `my_list = <PortalList> {\n    flow: Down\n    spacing: 5\n}`
    },
    'ScrollXView': {
        description: 'Horizontally scrollable container.',
        properties: ['width', 'height', 'flow', 'spacing'],
        example: `<ScrollXView> {\n    width: Fill\n    height: 100\n    flow: Right\n}`
    },
    'ScrollYView': {
        description: 'Vertically scrollable container.',
        properties: ['width', 'height', 'flow', 'spacing'],
        example: `<ScrollYView> {\n    width: Fill\n    height: Fill\n    flow: Down\n}`
    },
    'Window': {
        description: 'Top-level window widget.',
        properties: ['window', 'body'],
        example: `main_window = <Window> {\n    window: {inner_size: vec2(800, 600)}\n}`
    },
    'Root': {
        description: 'Root container that manages multiple windows.',
        properties: [],
        example: `<Root> {\n    main_window = <Window> { ... }\n}`
    },
    'Modal': {
        description: 'Modal overlay that appears above other content.',
        properties: [],
        example: `<Modal> {\n    content = <View> { ... }\n}`
    },
    'DropDown': {
        description: 'Dropdown selection widget.',
        properties: ['labels', 'selected_index'],
        example: `my_dropdown = <DropDown> {\n    labels: ["Option 1", "Option 2"]\n}`
    },
    'RadioButton': {
        description: 'Radio button for single-selection groups.',
        properties: ['text'],
        example: `my_radio = <RadioButton> {\n    text: "Option A"\n}`
    },
    'TabBar': {
        description: 'Tab navigation bar.',
        properties: [],
        example: `<TabBar> {\n    tab1 = <Tab> { text: "Tab 1" }\n}`
    },
    'StackNavigation': {
        description: 'Stack-based navigation for mobile-style page transitions.',
        properties: [],
        example: `<StackNavigation> {\n    root_view = <StackNavigationView> { ... }\n}`
    },
    'Splitter': {
        description: 'Resizable divider between two panels.',
        properties: ['axis', 'split'],
        example: `<Splitter> {\n    axis: Horizontal\n}`
    },
    'ColorPicker': {
        description: 'Color selection widget with wheel and sliders.',
        properties: [],
        example: `<ColorPicker> {}`
    },
    'Icon': {
        description: 'Icon display widget using SVG paths.',
        properties: ['draw_icon'],
        example: `<Icon> {\n    draw_icon: { svg_file: dep("...") }\n}`
    },
    'Html': {
        description: 'HTML content renderer (subset of HTML).',
        properties: ['html'],
        example: `<Html> {\n    html: "<b>Bold</b> text"\n}`
    },
    'Markdown': {
        description: 'Markdown content renderer.',
        properties: ['markdown'],
        example: `<Markdown> {\n    markdown: "# Heading"\n}`
    },
    'Video': {
        description: 'Video playback widget.',
        properties: ['source'],
        example: `<Video> {\n    source: dep("...")\n}`
    },
    'Tooltip': {
        description: 'Tooltip that appears on hover.',
        properties: ['text'],
        example: `<Tooltip> {\n    text: "Helpful info"\n}`
    },
    'FoldButton': {
        description: 'Collapsible section toggle button.',
        properties: [],
        example: `<FoldButton> {}`
    },
    'ExpandablePanel': {
        description: 'Collapsible panel with animated expand/collapse.',
        properties: [],
        example: `<ExpandablePanel> {\n    header = <View> { ... }\n    body = <View> { ... }\n}`
    }
};

// Property documentation
const PROPERTY_DOCS: Record<string, { type: string; values: string[]; description: string }> = {
    'width': {
        type: 'Size',
        values: ['Fill', 'Fit', 'All', '<number>'],
        description: 'Width of the widget. Fill = expand, Fit = shrink to content.'
    },
    'height': {
        type: 'Size',
        values: ['Fill', 'Fit', 'All', '<number>'],
        description: 'Height of the widget. Fill = expand, Fit = shrink to content.'
    },
    'flow': {
        type: 'Flow',
        values: ['Down', 'Right', 'Overlay', 'RightWrap'],
        description: 'Direction children are laid out. Down = column, Right = row.'
    },
    'spacing': {
        type: 'f64',
        values: ['<number>'],
        description: 'Space between child widgets in pixels.'
    },
    'padding': {
        type: 'Padding',
        values: ['<number>', '{top: N, right: N, bottom: N, left: N}'],
        description: 'Inner spacing between widget edge and content.'
    },
    'margin': {
        type: 'Margin',
        values: ['<number>', '{top: N, right: N, bottom: N, left: N}'],
        description: 'Outer spacing around the widget.'
    },
    'align': {
        type: 'Align',
        values: ['{x: 0.0-1.0, y: 0.0-1.0}'],
        description: 'Alignment of children. {x: 0.5, y: 0.5} = centered.'
    },
    'show_bg': {
        type: 'bool',
        values: ['true', 'false'],
        description: 'Whether to render the background.'
    },
    'draw_bg': {
        type: 'DrawColor',
        values: ['{color: #HEX}', '{fn pixel(self) -> vec4 { ... }}'],
        description: 'Background drawing configuration.'
    },
    'text': {
        type: 'String',
        values: ['"text content"'],
        description: 'Text content for Label, Button, etc.'
    },
    'fit': {
        type: 'ImageFit',
        values: ['Stretch', 'Horizontal', 'Vertical', 'Smallest', 'Biggest', 'Size', 'Centered'],
        description: 'How the image is scaled to fit its container.'
    },
    'source': {
        type: 'LiveDependency',
        values: ['dep("crate://self/path")'],
        description: 'Resource path for images, videos, etc.'
    },
    'cursor': {
        type: 'MouseCursor',
        values: ['Hand', 'Arrow', 'Text', 'Move', 'Wait', 'Help', 'NotAllowed'],
        description: 'Mouse cursor style when hovering.'
    }
};

/**
 * Find Makepad widgets source path from various locations
 */
function findMakepadWidgetsPath(): string | null {
    const home = os.homedir();
    
    // 1. Check workspace folders for local Makepad checkout
    const workspaceFolders = vscode.workspace.workspaceFolders;
    if (workspaceFolders) {
        for (const folder of workspaceFolders) {
            // Check if makepad is a sibling directory
            const parentDir = path.dirname(folder.uri.fsPath);
            const makepadPath = path.join(parentDir, 'makepad', 'widgets', 'src');
            if (fs.existsSync(makepadPath)) {
                console.log('Found Makepad in workspace sibling:', makepadPath);
                return makepadPath;
            }
            
            // Check if we're inside makepad directory
            const inMakepadPath = path.join(folder.uri.fsPath, 'widgets', 'src');
            if (fs.existsSync(inMakepadPath)) {
                console.log('Found Makepad in workspace:', inMakepadPath);
                return inMakepadPath;
            }
        }
    }
    
    // 2. Check Cargo registry for published crate
    const cargoRegistry = path.join(home, '.cargo', 'registry', 'src');
    if (fs.existsSync(cargoRegistry)) {
        try {
            const registryDirs = fs.readdirSync(cargoRegistry);
            for (const registryDir of registryDirs) {
                const registryPath = path.join(cargoRegistry, registryDir);
                const crates = fs.readdirSync(registryPath);
                
                // Find makepad-widgets-* directory (get latest version)
                const makepadWidgets = crates
                    .filter(c => c.startsWith('makepad-widgets-'))
                    .sort()
                    .pop();
                
                if (makepadWidgets) {
                    const widgetsPath = path.join(registryPath, makepadWidgets, 'src');
                    if (fs.existsSync(widgetsPath)) {
                        console.log('Found Makepad in Cargo registry:', widgetsPath);
                        return widgetsPath;
                    }
                }
            }
        } catch (e) {
            console.log('Error scanning Cargo registry:', e);
        }
    }
    
    // 3. Check Cargo git checkouts (for git dependencies)
    const cargoGit = path.join(home, '.cargo', 'git', 'checkouts');
    if (fs.existsSync(cargoGit)) {
        try {
            const checkouts = fs.readdirSync(cargoGit);
            for (const checkout of checkouts) {
                if (checkout.toLowerCase().includes('makepad')) {
                    const checkoutPath = path.join(cargoGit, checkout);
                    const versions = fs.readdirSync(checkoutPath);
                    for (const version of versions) {
                        const widgetsPath = path.join(checkoutPath, version, 'widgets', 'src');
                        if (fs.existsSync(widgetsPath)) {
                            console.log('Found Makepad in Cargo git:', widgetsPath);
                            return widgetsPath;
                        }
                    }
                }
            }
        } catch (e) {
            console.log('Error scanning Cargo git:', e);
        }
    }
    
    // 4. Check common development locations
    const commonPaths = [
        path.join(home, 'makepad', 'widgets', 'src'),
        path.join(home, 'projects', 'makepad', 'widgets', 'src'),
        path.join(home, 'dev', 'makepad', 'widgets', 'src'),
        path.join(home, 'code', 'makepad', 'widgets', 'src'),
        path.join(home, 'Work', 'makepad', 'widgets', 'src'),
        path.join(home, 'src', 'makepad', 'widgets', 'src'),
    ];
    
    for (const commonPath of commonPaths) {
        if (fs.existsSync(commonPath)) {
            console.log('Found Makepad in common path:', commonPath);
            return commonPath;
        }
    }
    
    console.log('Makepad widgets source not found');
    return null;
}

/**
 * Scan Makepad source files to find widget and property definitions
 */
function scanMakepadSource(): void {
    MAKEPAD_WIDGETS_PATH = findMakepadWidgetsPath();
    
    if (!MAKEPAD_WIDGETS_PATH) {
        console.log('Makepad widgets path not found - Go-to-Definition will be limited');
        return;
    }

    try {
        const files = fs.readdirSync(MAKEPAD_WIDGETS_PATH).filter(f => f.endsWith('.rs'));
        
        for (const file of files) {
            const filePath = path.join(MAKEPAD_WIDGETS_PATH, file);
            const content = fs.readFileSync(filePath, 'utf8');
            const lines = content.split('\n');
            
            for (let i = 0; i < lines.length; i++) {
                const line = lines[i];
                
                // Find widget struct definitions: pub struct WidgetName {
                const structMatch = line.match(/^pub struct (\w+)\s*\{/);
                if (structMatch) {
                    const name = structMatch[1];
                    // Skip internal types
                    if (!name.endsWith('Ref') && !name.endsWith('Set') && !name.startsWith('Draw')) {
                        WIDGET_LOCATIONS[name] = {
                            file: filePath,
                            line: i + 1 // 1-indexed
                        };
                    }
                }
                
                // Find property definitions
                const propMatch = line.match(/#\[live.*?\]\s*(?:pub\s+)?(\w+):/);
                if (propMatch) {
                    const propName = propMatch[1];
                    if (!PROPERTY_LOCATIONS[propName]) {
                        PROPERTY_LOCATIONS[propName] = {
                            file: filePath,
                            line: i + 1
                        };
                    }
                }
            }
        }
        
        console.log(`Scanned Makepad: ${Object.keys(WIDGET_LOCATIONS).length} widgets, ${Object.keys(PROPERTY_LOCATIONS).length} properties`);
    } catch (e) {
        console.log('Error scanning Makepad source:', e);
    }
}

export function activate(context: vscode.ExtensionContext) {
    console.log('Makepad Live Design extension activated');
    
    // Scan Makepad source for definitions
    scanMakepadSource();

    // DEFINITION PROVIDER for Go-to-Definition (Cmd+Click)
    const definitionProvider = vscode.languages.registerDefinitionProvider('rust', {
        provideDefinition(document, position): vscode.ProviderResult<vscode.Definition> {
            const range = document.getWordRangeAtPosition(position);
            if (!range) return null;

            const word = document.getText(range);
            
            // Check if inside live_design! macro
            const textBefore = document.getText(new vscode.Range(0, 0, position.line, position.character));
            if (!textBefore.includes('live_design!')) {
                return null;
            }

            // Widget names
            if (WIDGET_LOCATIONS[word]) {
                const loc = WIDGET_LOCATIONS[word];
                if (fs.existsSync(loc.file)) {
                    return new vscode.Location(
                        vscode.Uri.file(loc.file),
                        new vscode.Position(loc.line - 1, 0)
                    );
                }
            }

            // Property names
            if (PROPERTY_LOCATIONS[word]) {
                const loc = PROPERTY_LOCATIONS[word];
                if (fs.existsSync(loc.file)) {
                    return new vscode.Location(
                        vscode.Uri.file(loc.file),
                        new vscode.Position(loc.line - 1, 0)
                    );
                }
            }

            // Enum values - search in discovered Makepad path
            if (MAKEPAD_WIDGETS_PATH) {
                const enumLocations: Record<string, { file: string; pattern: string }> = {
                    'Fill': { file: 'view.rs', pattern: 'Fill' },
                    'Fit': { file: 'view.rs', pattern: 'Fit' },
                    'Down': { file: 'view.rs', pattern: 'Down' },
                    'Right': { file: 'view.rs', pattern: 'Right' },
                    'Overlay': { file: 'view.rs', pattern: 'Overlay' },
                    'Centered': { file: 'image_cache.rs', pattern: 'Centered' },
                    'Smallest': { file: 'image_cache.rs', pattern: 'Smallest' },
                    'Biggest': { file: 'image_cache.rs', pattern: 'Biggest' },
                    'Stretch': { file: 'image_cache.rs', pattern: 'Stretch' },
                };

                if (enumLocations[word]) {
                    const enumInfo = enumLocations[word];
                    const filePath = path.join(MAKEPAD_WIDGETS_PATH, enumInfo.file);
                    if (fs.existsSync(filePath)) {
                        const content = fs.readFileSync(filePath, 'utf8');
                        const lines = content.split('\n');
                        for (let i = 0; i < lines.length; i++) {
                            if (lines[i].includes(enumInfo.pattern) && lines[i].includes('#[')) {
                                return new vscode.Location(
                                    vscode.Uri.file(filePath),
                                    new vscode.Position(i, 0)
                                );
                            }
                        }
                    }
                }
            }

            return null;
        }
    });

    // HOVER PROVIDER
    const hoverProvider = vscode.languages.registerHoverProvider('rust', {
        provideHover(document, position) {
            const range = document.getWordRangeAtPosition(position);
            if (!range) return null;

            const word = document.getText(range);

            // Check if inside live_design! macro
            const textBefore = document.getText(new vscode.Range(0, 0, position.line, position.character));
            if (!textBefore.includes('live_design!')) {
                return null;
            }

            // Widget docs
            if (WIDGET_DOCS[word]) {
                const widget = WIDGET_DOCS[word];
                const markdown = new vscode.MarkdownString();
                markdown.appendMarkdown(`## ${word}\n\n`);
                markdown.appendMarkdown(`${widget.description}\n\n`);
                
                if (widget.properties.length > 0) {
                    markdown.appendMarkdown(`**Properties:** \`${widget.properties.join('`, `')}\`\n\n`);
                }
                
                if (WIDGET_LOCATIONS[word]) {
                    const loc = WIDGET_LOCATIONS[word];
                    markdown.appendMarkdown(`**Source:** \`${path.basename(loc.file)}:${loc.line}\`\n\n`);
                }
                
                markdown.appendMarkdown(`**Example:**\n\`\`\`rust\n${widget.example}\n\`\`\``);
                return new vscode.Hover(markdown, range);
            }

            // Property docs
            if (PROPERTY_DOCS[word]) {
                const prop = PROPERTY_DOCS[word];
                const markdown = new vscode.MarkdownString();
                markdown.appendMarkdown(`## ${word}\n\n`);
                markdown.appendMarkdown(`**Type:** \`${prop.type}\`\n\n`);
                markdown.appendMarkdown(`${prop.description}\n\n`);
                markdown.appendMarkdown(`**Values:** \`${prop.values.join('`, `')}\``);
                return new vscode.Hover(markdown, range);
            }

            return null;
        }
    });

    // COMPLETION PROVIDER
    const completionProvider = vscode.languages.registerCompletionItemProvider('rust', {
        provideCompletionItems(document, position, _token, context) {
            const textBefore = document.getText(new vscode.Range(0, 0, position.line, position.character));
            
            if (!textBefore.includes('live_design!')) {
                return [];
            }

            const items: vscode.CompletionItem[] = [];
            const line = document.lineAt(position.line).text;
            const charBefore = line.substring(0, position.character);

            // Check if triggered by specific character or explicitly invoked
            const isTriggerCharacter = context.triggerKind === vscode.CompletionTriggerKind.TriggerCharacter;
            const isExplicitInvoke = context.triggerKind === vscode.CompletionTriggerKind.Invoke;

            // After '<' - suggest widgets (only on trigger character '<')
            if (charBefore.match(/<\s*$/) && (isTriggerCharacter || isExplicitInvoke)) {
                for (const [name, widget] of Object.entries(WIDGET_DOCS)) {
                    const item = new vscode.CompletionItem(name, vscode.CompletionItemKind.Class);
                    item.detail = 'Makepad Widget';
                    item.documentation = new vscode.MarkdownString(widget.description);
                    item.insertText = new vscode.SnippetString(`${name}> {\n\t$0\n}`);
                    items.push(item);
                }
                
                // Add widgets from scanned source
                for (const name of Object.keys(WIDGET_LOCATIONS)) {
                    if (!WIDGET_DOCS[name]) {
                        const item = new vscode.CompletionItem(name, vscode.CompletionItemKind.Class);
                        item.detail = 'Makepad Widget';
                        item.insertText = new vscode.SnippetString(`${name}> {\n\t$0\n}`);
                        items.push(item);
                    }
                }
                return items;
            }

            // After property: - suggest values (only on trigger character ':')
            const propMatch = charBefore.match(/(\w+):\s*$/);
            if (propMatch && (isTriggerCharacter || isExplicitInvoke)) {
                const propName = propMatch[1];
                const prop = PROPERTY_DOCS[propName];
                if (prop) {
                    for (const value of prop.values) {
                        if (!value.startsWith('<') && !value.startsWith('{')) {
                            const item = new vscode.CompletionItem(value, vscode.CompletionItemKind.Value);
                            item.detail = propName;
                            items.push(item);
                        }
                    }
                }
                return items;
            }

            // Inside widget - suggest properties (ONLY on explicit invoke Ctrl/Cmd+Space)
            if (isExplicitInvoke && (charBefore.match(/^\s*$/) || charBefore.match(/{\s*$/))) {
                for (const [name, prop] of Object.entries(PROPERTY_DOCS)) {
                    const item = new vscode.CompletionItem(name, vscode.CompletionItemKind.Property);
                    item.detail = prop.type;
                    item.documentation = new vscode.MarkdownString(prop.description);
                    
                    if (name === 'align') {
                        item.insertText = new vscode.SnippetString(`${name}: {x: \${1:0.5}, y: \${2:0.5}}`);
                    } else if (name === 'padding' || name === 'margin') {
                        item.insertText = new vscode.SnippetString(`${name}: \${1:10}`);
                    } else if (name === 'draw_bg') {
                        item.insertText = new vscode.SnippetString(`${name}: {\n\tcolor: \${1:#333}\n}`);
                    } else if (prop.values.length > 1) {
                        item.insertText = new vscode.SnippetString(`${name}: \${1|${prop.values.join(',')}|}`);
                    } else {
                        item.insertText = new vscode.SnippetString(`${name}: \${1:value}`);
                    }
                    items.push(item);
                }
            }

            return items;
        }
    }, '<', ':');

    context.subscriptions.push(definitionProvider, hoverProvider, completionProvider);
}

export function deactivate() {}
