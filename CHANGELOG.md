# Changelog

All notable changes to the Makepad Live Design extension.

## [0.2.0] - 2024-12-12

### Added
- **Go-to-Definition** (Cmd+Click / Ctrl+Click)
  - Jump to widget struct definitions (`View`, `Button`, `Image`, etc.)
  - Jump to property definitions (`width`, `height`, `align`, etc.)
  - Jump to enum value definitions (`Fill`, `Fit`, `Centered`, etc.)
- **Dynamic Makepad Source Discovery**
  - Automatically finds Makepad widgets in Cargo registry
  - Falls back to common local development paths
  - No manual configuration required
- **Source Location in Hover**
  - Hover tooltips now show file and line number for widgets

### Changed
- Extension now scans Makepad source at activation time
- Autocomplete includes widgets discovered from source (not just documented ones)

## [0.1.0] - 2024-12-12

### Added
- **73 Snippets** for rapid Makepad development
  - Widget snippets (`mpview`, `mpbutton`, `mplabel`, etc.)
  - Property snippets (`wfill`, `hfit`, `flowdown`, etc.)
  - Layout snippets (`mplayouth`, `mplayoutv`, `mpcenter`, etc.)
  - Rust code snippets (`mpwidgetstruct`, `mpwidgetimpl`, etc.)
- **Hover Documentation**
  - Widget descriptions and examples
  - Property types and allowed values
- **Smart Autocomplete**
  - Widget suggestions after `<`
  - Property suggestions inside `{}`
  - Value suggestions after `property:`
- **Python Script** to regenerate snippets from Makepad source

## Future Plans
- [ ] Diagnostics for invalid widget/property names
- [ ] Rename symbol support
- [ ] Find all references
- [ ] Live preview integration with Makepad Studio

