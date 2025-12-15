# Makepad Live Design - VS Code / Cursor Extension

Enhanced development experience for Makepad's `live_design!` macro — **without a full LSP**.

## Features

### ✨ Go-to-Definition (Cmd+Click / Ctrl+Click)

Jump directly to Makepad source code:
- **Widgets**: `View`, `Button`, `Image`, `Label`, etc. → Opens widget struct definition
- **Properties**: `width`, `height`, `align`, etc. → Opens property definition
- **Values**: `Fill`, `Fit`, `Centered`, etc. → Opens enum definition

### 📝 Hover Documentation

Hover over any widget or property to see:
- Description
- Available properties
- Source file location
- Code example

### 🔧 Smart Autocomplete

- After `<` → Widget suggestions with descriptions
- Inside `{}` → Property suggestions with types
- After `property:` → Value suggestions

### 🚀 73 Snippets

Type prefixes and press Tab:

| Category | Examples |
|----------|----------|
| Widgets | `mpview`, `mpbutton`, `mplabel`, `mpimage` |
| Layout | `mplayouth`, `mplayoutv`, `mpcenter` |
| Properties | `wfill`, `hfit`, `flowdown`, `aligncenter` |
| Rust Code | `mpwidgetstruct`, `mpwidgetimpl`, `app_main` |

## Installation

### Option 1: Development Mode (Recommended for Testing)

Run the extension directly from source - changes take effect immediately after reload:

```bash
# Clone and build
git clone https://github.com/amitsheokand/makepad-vscode-extension.git
cd makepad-vscode-extension
npm install
npm run compile

# Launch VS Code/Cursor with extension loaded
code --extensionDevelopmentPath="$(pwd)"
# or for Cursor:
cursor --extensionDevelopmentPath="$(pwd)"
```

### Option 2: Install to Extensions Directory

Copy the built extension to your editor's extensions folder:

```bash
# Clone and build
git clone https://github.com/amitsheokand/makepad-vscode-extension.git
cd makepad-vscode-extension
npm install
npm run compile
```

**For Cursor:**
```bash
EXT_DIR="$HOME/.cursor/extensions/makepad-live-design"
mkdir -p "$EXT_DIR/out"
cp package.json "$EXT_DIR/"
cp -r snippets "$EXT_DIR/"
cp -r syntaxes "$EXT_DIR/"
cp out/extension.js "$EXT_DIR/out/"
```

**For VS Code:**
```bash
EXT_DIR="$HOME/.vscode/extensions/makepad-live-design"
mkdir -p "$EXT_DIR/out"
cp package.json "$EXT_DIR/"
cp -r snippets "$EXT_DIR/"
cp -r syntaxes "$EXT_DIR/"
cp out/extension.js "$EXT_DIR/out/"
```

**Restart your editor** (Cmd+Q / Ctrl+Q, then reopen) to activate.

### Option 3: Package as VSIX

Create a portable `.vsix` file that can be shared or installed via UI:

```bash
# Install vsce if not already installed
npm install -g @vscode/vsce

# Package the extension
cd makepad-vscode-extension
vsce package

# Install via command line
code --install-extension makepad-live-design-0.2.0.vsix
# or for Cursor:
cursor --install-extension makepad-live-design-0.2.0.vsix
```

Or install via UI: Extensions → "..." menu → "Install from VSIX..."

## How Makepad Source is Found

The extension automatically searches for Makepad widgets in this order:

1. **Workspace sibling**: `../makepad/widgets/src/` (for local development)
2. **Cargo registry**: `~/.cargo/registry/src/*/makepad-widgets-*/src/`
3. **Cargo git checkout**: `~/.cargo/git/checkouts/makepad-*/*/widgets/src/`
4. **Common paths**: `~/makepad/`, `~/projects/makepad/`, `~/dev/makepad/`, etc.

No manual configuration needed!

## Snippet Reference

### Widget Snippets

| Prefix | Widget | Example |
|--------|--------|---------|
| `mpview` | View | Container with layout |
| `mpbutton` | Button | Clickable button |
| `mplabel` | Label | Text display |
| `mpimage` | Image | Image display |
| `mptextinput` | TextInput | Text input field |
| `mpcheckbox` | CheckBox | Toggle checkbox |
| `mpslider` | Slider | Numeric slider |
| `mpportallist` | PortalList | Virtualized list |
| `mpscrollx` | ScrollXView | Horizontal scroll |
| `mpscrolly` | ScrollYView | Vertical scroll |
| `mproot` | Root + Window | App root structure |

### Property Snippets

| Prefix | Output |
|--------|--------|
| `wfill` | `width: Fill` |
| `wfit` | `width: Fit` |
| `hfill` | `height: Fill` |
| `hfit` | `height: Fit` |
| `flowdown` | `flow: Down` |
| `flowright` | `flow: Right` |
| `aligncenter` | `align: {x: 0.5, y: 0.5}` |
| `mpspacing` | `spacing: 5` |
| `mppadding` | `padding: 10` |
| `mpshowbg` | `show_bg: true` + `draw_bg: {...}` |

### Rust Code Snippets

| Prefix | Description |
|--------|-------------|
| `live_design` | Full `live_design!` block |
| `mpwidgetstruct` | Widget struct with derives |
| `mpwidgetimpl` | Widget trait implementation |
| `mpwidgetmatch` | WidgetMatchEvent implementation |
| `mpbtnclick` | Button click handler |
| `mpkeydown` | Keyboard event handler |
| `mpfingerdown` | Mouse/touch handler |
| `mpimgload` | Async image load |
| `mpportallistdraw` | PortalList draw pattern |

## Requirements

- Makepad installed via Cargo or cloned locally
- VS Code / Cursor with Rust support

## Known Limitations

- Go-to-Definition only works inside `live_design!` macro
- Custom widgets in your project aren't indexed (only makepad-widgets)
- Some enum values may not resolve if files are renamed in Makepad

## Contributing

Feel free to add more snippets or improve the extension!

```bash
# Regenerate snippets from Makepad source
python3 scripts/extract_widgets.py
```

## Resources

- [Makepad Repository](https://github.com/makepad/makepad)
- [Makepad Studio](https://github.com/makepad/makepad/tree/main/studio) - Official IDE with live reload
- [CHANGELOG](./CHANGELOG.md)
