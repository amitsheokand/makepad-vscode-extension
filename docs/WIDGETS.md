# Makepad Widgets Reference

Auto-generated from Makepad source code.

## Table of Contents

- [AdaptiveView](#adaptiveview)
- [BareStep](#barestep)
- [Button](#button)
- [CachedWidget](#cachedwidget)
- [CheckBox](#checkbox)
- [ColorPicker](#colorpicker)
- [CommandTextInput](#commandtextinput)
- [DebugView](#debugview)
- [Designer](#designer)
- [DesignerContainer](#designercontainer)
- [DesignerOutline](#designeroutline)
- [DesignerOutlineTree](#designeroutlinetree)
- [DesignerOutlineTreeNode](#designeroutlinetreenode)
- [DesignerToolbox](#designertoolbox)
- [DesignerView](#designerview)
- [DesktopButton](#desktopbutton)
- [Dock](#dock)
- [DropDown](#dropdown)
- [ExpandablePanel](#expandablepanel)
- [FileTree](#filetree)
- [FileTreeNode](#filetreenode)
- [FlatList](#flatlist)
- [FoldButton](#foldbutton)
- [FoldHeader](#foldheader)
- [Html](#html)
- [HtmlLink](#htmllink)
- [Icon](#icon)
- [Image](#image)
- [ImageBlend](#imageblend)
- [KeyboardView](#keyboardview)
- [Label](#label)
- [LinkLabel](#linklabel)
- [Markdown](#markdown)
- [Modal](#modal)
- [MultiImage](#multiimage)
- [MultiWindow](#multiwindow)
- [NavControl](#navcontrol)
- [PageFlip](#pageflip)
- [PerformanceLiveGraph](#performancelivegraph)
- [PerformanceView](#performanceview)
- [PopupMenu](#popupmenu)
- [PopupMenuItem](#popupmenuitem)
- [PopupNotification](#popupnotification)
- [PortalList](#portallist)
- [PortalList2](#portallist2)
- [RadioButton](#radiobutton)
- [RadioButtonGroup](#radiobuttongroup)
- [Root](#root)
- [RotatedImage](#rotatedimage)
- [ScrollBar](#scrollbar)
- [ScrollBars](#scrollbars)
- [SlidePanel](#slidepanel)
- [Slider](#slider)
- [SlidesView](#slidesview)
- [Splitter](#splitter)
- [StackNavigation](#stacknavigation)
- [StackNavigationView](#stacknavigationview)
- [Tab](#tab)
- [TabBar](#tabbar)
- [TabCloseButton](#tabclosebutton)
- [TextFlow](#textflow)
- [TextInput](#textinput)
- [TogglePanel](#togglepanel)
- [Tooltip](#tooltip)
- [TurtleStep](#turtlestep)
- [VectorLine](#vectorline)
- [VectorSpline](#vectorspline)
- [Video](#video)
- [View](#view)
- [WebView](#webview)
- [Window](#window)
- [WindowMenu](#windowmenu)
- [XrHands](#xrhands)

---

## AdaptiveView

**File:** `adaptive_view.rs`

 In this example, the `AdaptiveView` switches between Desktop and Mobile layouts based on the screen width. The `set_variant_selector` method allows you to define custom logic for choosing the appropriate layout variant.  `AdaptiveView` implements a default variant selector based on the screen width for different device layouts (Currently `Desktop` and `Mobile`). You can override this through the `set_variant_selector` method.  Check out [VariantSelector] for more information on how to define custom selectors, and what information is available to them.

### Properties

| Property | Type | Default |
|----------|------|--------|
| `retain_unused_variants` | `bool` | - |

### Example

```rust
my_adaptiveview = <AdaptiveView> {
    // properties here
}
```

---

## BareStep

**File:** `bare_step.rs`

### Example

```rust
my_barestep = <BareStep> {
    // properties here
}
```

---

## Button

**File:** `button.rs`

A clickable button widget that emits actions when pressed, and when either released or clicked.

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |
| `draw_text` | `DrawText` | - |
| `draw_icon` | `DrawIcon` | - |
| `icon_walk` | `Walk` | - |
| `label_walk` | `Walk` | - |
| `grab_key_focus` | `bool` | true |
| `enabled` | `bool` | true |
| `enable_long_press` | `bool` | - |
| `reset_hover_on_click` | `bool` | - |
| `text` | `ArcStringMut` | - |

### Example

```rust
my_button = <Button> {
    // properties here
}
```

---

## CachedWidget

**File:** `cached_widget.rs`

 - Uses a global `WidgetWrapperCache` to store cached widgets - Handles widget creation and caching in the `after_apply` hook - Delegates most widget operations (like event handling and drawing) to the cached child widget  # Note  While `CachedWidget` can significantly improve performance for complex, frequently used widgets, it should be used judiciously. Overuse of caching can lead to unexpected behavior if not managed properly.

### Example

```rust
my_cachedwidget = <CachedWidget> {
    // properties here
}
```

---

## CheckBox

**File:** `check_box.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `icon_walk` | `Walk` | - |
| `label_walk` | `Walk` | - |
| `label_align` | `Align` | - |
| `draw_bg` | `DrawCheckBox` | - |
| `draw_text` | `DrawText` | - |
| `draw_icon` | `DrawIcon` | - |
| `text` | `ArcStringMut` | - |
| `visible` | `bool` | true |
| `active` | `Option<bool>` | None |
| `bind` | `String` | - |

### Example

```rust
my_checkbox = <CheckBox> {
    // properties here
}
```

---

## ColorPicker

**File:** `color_picker.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_wheel` | `DrawColorWheel` | - |

### Example

```rust
my_colorpicker = <ColorPicker> {
    // properties here
}
```

---

## CommandTextInput

**File:** `command_text_input.rs`

`TextInput` wrapper glued to a popup list of options that is shown when a trigger character is typed.  Limitation: Selectable items are expected to be `View`s.

### Properties

| Property | Type | Default |
|----------|------|--------|
| `trigger` | `Option<String>` | - |
| `inline_search` | `bool` | - |
| `color_focus` | `Vec4` | - |
| `color_hover` | `Vec4` | - |

### Example

```rust
my_commandtextinput = <CommandTextInput> {
    // properties here
}
```

---

## DebugView

**File:** `debug_view.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_list` | `DrawList2d` | - |
| `rect` | `DrawRect` | - |
| `label` | `DrawText` | - |

### Example

```rust
my_debugview = <DebugView> {
    // properties here
}
```

---

## Designer

**File:** `designer.rs`

### Example

```rust
my_designer = <Designer> {
    // properties here
}
```

---

## DesignerContainer

**File:** `designer_view.rs`

### Example

```rust
my_designercontainer = <DesignerContainer> {
    // properties here
}
```

---

## DesignerOutline

**File:** `designer_outline.rs`

### Example

```rust
my_designeroutline = <DesignerOutline> {
    // properties here
}
```

---

## DesignerOutlineTree

**File:** `designer_outline_tree.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `scroll_bars` | `ScrollBars` | - |
| `filler` | `DrawNodeQuad` | - |
| `node_height` | `f64` | - |
| `draw_scroll_shadow` | `DrawScrollShadow` | - |

### Example

```rust
my_designeroutlinetree = <DesignerOutlineTree> {
    // properties here
}
```

---

## DesignerOutlineTreeNode

**File:** `designer_outline_tree.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawNodeQuad` | - |
| `button_open` | `FoldButton` | - |
| `draw_icon` | `DrawNodeIcon` | - |
| `draw_text` | `DrawNodeText` | - |
| `icon_walk` | `Walk` | - |
| `button_open_width` | `f64` | - |
| `draw_eye` | `bool` | - |
| `min_drag_distance` | `f64` | - |
| `indent_width` | `f64` | - |
| `indent_shift` | `f64` | - |
| `selected` | `f64` | - |
| `opened` | `f64` | - |
| `hover` | `f64` | - |
| `focussed` | `f64` | - |

### Example

```rust
my_designeroutlinetreenode = <DesignerOutlineTreeNode> {
    // properties here
}
```

---

## DesignerToolbox

**File:** `designer_toolbox.rs`

### Example

```rust
my_designertoolbox = <DesignerToolbox> {
    // properties here
}
```

---

## DesignerView

**File:** `designer_view.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `clear_color` | `Vec4` | - |
| `container` | `Option<LivePtr>` | - |
| `draw_bg` | `DrawColor` | - |
| `draw_outline` | `DrawQuad` | - |

### Example

```rust
my_designerview = <DesignerView> {
    // properties here
}
```

---

## DesktopButton

**File:** `desktop_button.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawDesktopButton` | - |

### Example

```rust
my_desktopbutton = <DesktopButton> {
    // properties here
}
```

---

## Dock

**File:** `dock.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `drop_target_draw_list` | `DrawList2d` | - |
| `round_corner` | `DrawRoundCorner` | - |
| `drag_target_preview` | `DrawColor` | - |
| `tab_bar` | `Option<LivePtr>` | - |
| `splitter` | `Option<LivePtr>` | - |

### Example

```rust
my_dock = <Dock> {
    // properties here
}
```

---

## DropDown

**File:** `drop_down.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |
| `draw_text` | `DrawLabelText` | - |
| `bind` | `String` | - |
| `bind_enum` | `String` | - |
| `popup_menu` | `Option<LivePtr>` | - |
| `labels` | `Vec<String>` | - |
| `values` | `Vec<LiveValue>` | - |
| `popup_menu_position` | `PopupMenuPosition` | - |
| `selected_item` | `usize` | - |

### Example

```rust
my_dropdown = <DropDown> {
    // properties here
}
```

---

## ExpandablePanel

**File:** `expandable_panel.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `initial_offset` | `f64` | - |

### Example

```rust
my_expandablepanel = <ExpandablePanel> {
    // properties here
}
```

---

## FileTree

**File:** `file_tree.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `scroll_bars` | `ScrollBars` | - |
| `file_node` | `Option<LivePtr>` | - |
| `folder_node` | `Option<LivePtr>` | - |
| `filler` | `DrawBgQuad` | - |
| `node_height` | `f64` | - |
| `draw_scroll_shadow` | `DrawScrollShadow` | - |

### Example

```rust
my_filetree = <FileTree> {
    // properties here
}
```

---

## FileTreeNode

**File:** `file_tree.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawBgQuad` | - |
| `draw_icon` | `DrawIconQuad` | - |
| `draw_text` | `DrawNameText` | - |
| `check_box` | `CheckBox` | - |
| `indent_width` | `f64` | - |
| `indent_shift` | `f64` | - |
| `icon_walk` | `Walk` | - |
| `is_folder` | `bool` | - |
| `min_drag_distance` | `f64` | - |
| `opened` | `f32` | - |
| `focussed` | `f32` | - |
| `hover` | `f32` | - |
| `active` | `f32` | - |

### Example

```rust
my_filetreenode = <FileTreeNode> {
    // properties here
}
```

---

## FlatList

**File:** `flat_list.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `flick_scroll_minimum` | `f64` | 0.2 |
| `flick_scroll_maximum` | `f64` | 80.0 |
| `flick_scroll_scaling` | `f64` | 0.005 |
| `flick_scroll_decay` | `f64` | 0.98 |
| `swipe_drag_duration` | `f64` | 0.2 |
| `max_pull_down` | `f64` | 100.0 |
| `align_top_when_empty` | `bool` | true |
| `grab_key_focus` | `bool` | false |
| `drag_scrolling` | `bool` | true |
| `scroll_bars` | `ScrollBars` | - |
| `capture_overload` | `bool` | - |

### Example

```rust
my_flatlist = <FlatList> {
    // properties here
}
```

---

## FoldButton

**File:** `fold_button.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |
| `abs_size` | `DVec2` | - |
| `abs_offset` | `DVec2` | - |
| `active` | `f64` | - |

### Example

```rust
my_foldbutton = <FoldButton> {
    // properties here
}
```

---

## FoldHeader

**File:** `fold_header.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `header` | `WidgetRef` | - |
| `body` | `WidgetRef` | - |
| `opened` | `f64` | - |
| `body_walk` | `Walk` | - |

### Example

```rust
my_foldheader = <FoldHeader> {
    // properties here
}
```

---

## Html

**File:** `html.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `body` | `ArcStringMut` | - |
| `ul_markers` | `Vec<String>` | - |
| `ol_markers` | `Vec<OrderedListType>` | - |
| `ol_separator` | `String` | - |

### Example

```rust
my_html = <Html> {
    // properties here
}
```

---

## HtmlLink

**File:** `html.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `grab_key_focus` | `bool` | true |
| `hovered` | `f32` | - |
| `pressed` | `f32` | - |
| `color` | `Option<Vec4>` | - |
| `hover_color` | `Option<Vec4>` | - |
| `pressed_color` | `Option<Vec4>` | - |
| `text` | `ArcStringMut` | - |
| `url` | `String` | - |

### Example

```rust
my_htmllink = <HtmlLink> {
    // properties here
}
```

---

## Icon

**File:** `icon.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |
| `draw_icon` | `DrawIcon` | - |
| `icon_walk` | `Walk` | - |

### Example

```rust
my_icon = <Icon> {
    // properties here
}
```

---

## Image

**File:** `image.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawImage` | - |
| `min_width` | `i64` | - |
| `min_height` | `i64` | - |
| `width_scale` | `f64` | 1.0 |
| `visible` | `bool` | true |
| `fit` | `ImageFit` | - |
| `source` | `LiveDependency` | - |

### Example

```rust
my_image = <Image> {
    // properties here
}
```

---

## ImageBlend

**File:** `image_blend.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `image_a` | `Image` | - |
| `image_b` | `Image` | - |

### Example

```rust
my_imageblend = <ImageBlend> {
    // properties here
}
```

---

## KeyboardView

**File:** `keyboard_view.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `outer_layout` | `Layout` | - |
| `outer_walk` | `Walk` | - |
| `keyboard_walk` | `Walk` | - |
| `keyboard_min_shift` | `f64` | - |

### Example

```rust
my_keyboardview = <KeyboardView> {
    // properties here
}
```

---

## Label

**File:** `label.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_text` | `DrawText` | - |
| `align` | `Align` | - |
| `flow` | `Flow` | Flow::RightWrap |
| `padding` | `Padding` | - |
| `text` | `ArcStringMut` | - |
| `hover_actions_enabled` | `bool` | false |

### Example

```rust
my_label = <Label> {
    // properties here
}
```

---

## LinkLabel

**File:** `link_label.rs`

A clickable label widget that opens a URL when clicked.  This is a wrapper around (and derefs to) a [`Button`] widget.

### Properties

| Property | Type | Default |
|----------|------|--------|
| `url` | `String` | - |
| `open_in_place` | `bool` | - |

### Example

```rust
my_linklabel = <LinkLabel> {
    // properties here
}
```

---

## Markdown

**File:** `markdown.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `body` | `ArcStringMut` | - |
| `paragraph_spacing` | `f64` | - |
| `pre_code_spacing` | `f64` | - |
| `use_code_block_widget` | `bool` | false |

### Example

```rust
my_markdown = <Markdown> {
    // properties here
}
```

---

## Modal

**File:** `modal.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |

### Example

```rust
my_modal = <Modal> {
    // properties here
}
```

---

## MultiImage

**File:** `multi_image.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |
| `min_width` | `i64` | - |
| `min_height` | `i64` | - |
| `width_scale` | `f64` | 1.0 |
| `fit` | `ImageFit` | - |
| `source1` | `LiveDependency` | - |
| `source2` | `LiveDependency` | - |
| `source3` | `LiveDependency` | - |
| `source4` | `LiveDependency` | - |

### Example

```rust
my_multiimage = <MultiImage> {
    // properties here
}
```

---

## MultiWindow

**File:** `multi_window.rs`

### Example

```rust
my_multiwindow = <MultiWindow> {
    // properties here
}
```

---

## NavControl

**File:** `nav_control.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_list` | `DrawList2d` | - |
| `draw_focus` | `DrawQuad` | - |
| `draw_text` | `DrawText` | - |

### Example

```rust
my_navcontrol = <NavControl> {
    // properties here
}
```

---

## PageFlip

**File:** `page_flip.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `lazy_init` | `bool` | false |
| `active_page` | `LiveId` | - |

### Example

```rust
my_pageflip = <PageFlip> {
    // properties here
}
```

---

## PerformanceLiveGraph

**File:** `performance_view.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_graph` | `DrawColor` | - |
| `draw_bar` | `DrawColor` | - |
| `bar_width` | `f64` | - |
| `data_increments` | `i64` | - |
| `data_y_suffix` | `String` | - |
| `graph_label` | `String` | - |

### Example

```rust
my_performancelivegraph = <PerformanceLiveGraph> {
    // properties here
}
```

---

## PerformanceView

**File:** `performance_view.rs`

### Example

```rust
my_performanceview = <PerformanceView> {
    // properties here
}
```

---

## PopupMenu

**File:** `popup_menu.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_list` | `DrawList2d` | - |
| `menu_item` | `Option<LivePtr>` | - |
| `draw_bg` | `DrawQuad` | - |
| `items` | `Vec<String>` | - |

### Example

```rust
my_popupmenu = <PopupMenu> {
    // properties here
}
```

---

## PopupMenuItem

**File:** `popup_menu.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |
| `draw_text` | `DrawText` | - |
| `indent_width` | `f32` | - |
| `icon_walk` | `Walk` | - |
| `opened` | `f32` | - |
| `hover` | `f32` | - |
| `active` | `f32` | - |

### Example

```rust
my_popupmenuitem = <PopupMenuItem> {
    // properties here
}
```

---

## PopupNotification

**File:** `popup_notification.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |

### Example

```rust
my_popupnotification = <PopupNotification> {
    // properties here
}
```

---

## PortalList

**File:** `portal_list.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `flick_scroll_minimum` | `f64` | 0.2 |
| `flick_scroll_maximum` | `f64` | 80.0 |
| `flick_scroll_scaling` | `f64` | 0.005 |
| `flick_scroll_decay` | `f64` | 0.97 |
| `max_pull_down` | `f64` | 80.0 |
| `align_top_when_empty` | `bool` | true |
| `grab_key_focus` | `bool` | false |
| `drag_scrolling` | `bool` | true |
| `scroll_bar` | `ScrollBar` | - |
| `capture_overload` | `bool` | - |
| `keep_invisible` | `bool` | false |
| `auto_tail` | `bool` | false |
| `draw_caching` | `bool` | false |
| `reuse_items` | `bool` | false |

### Example

```rust
my_portallist = <PortalList> {
    // properties here
}
```

---

## PortalList2

**File:** `portal_list2.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `flick_scroll_minimum` | `f64` | 0.2 |
| `flick_scroll_maximum` | `f64` | 80.0 |
| `flick_scroll_scaling` | `f64` | 0.005 |
| `flick_scroll_decay` | `f64` | 0.98 |
| `max_pull_down` | `f64` | 100.0 |
| `grab_key_focus` | `bool` | false |
| `capture_overload` | `bool` | - |
| `drag_scrolling` | `bool` | true |
| `auto_tail` | `bool` | false |
| `scroll_bar` | `ScrollBar` | - |

### Example

```rust
my_portallist2 = <PortalList2> {
    // properties here
}
```

---

## RadioButton

**File:** `radio_button.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawRadioButton` | - |
| `draw_icon` | `DrawIcon` | - |
| `draw_text` | `DrawText` | - |
| `value` | `LiveValue` | - |
| `media` | `MediaType` | - |
| `icon_walk` | `Walk` | - |
| `image` | `Image` | - |
| `label_walk` | `Walk` | - |
| `label_align` | `Align` | - |
| `text` | `ArcStringMut` | - |
| `bind` | `String` | - |

### Example

```rust
my_radiobutton = <RadioButton> {
    // properties here
}
```

---

## RadioButtonGroup

**File:** `radio_button.rs`

### Example

```rust
my_radiobuttongroup = <RadioButtonGroup> {
    // properties here
}
```

---

## Root

**File:** `root.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `xr_pass` | `Pass` | - |

### Example

```rust
my_root = <Root> {
    // properties here
}
```

---

## RotatedImage

**File:** `rotated_image.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawColor` | - |
| `source` | `LiveDependency` | - |
| `scale` | `f64` | - |

### Example

```rust
my_rotatedimage = <RotatedImage> {
    // properties here
}
```

---

## ScrollBar

**File:** `scroll_bar.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawScrollBar` | - |
| `bar_size` | `f64` | - |
| `min_handle_size` | `f64` | - |
| `bar_side_margin` | `f64` | - |
| `axis` | `ScrollAxis` | ScrollAxis::Horizontal |
| `use_vertical_finger_scroll` | `bool` | - |
| `smoothing` | `Option<f64>` | - |

### Example

```rust
my_scrollbar = <ScrollBar> {
    // properties here
}
```

---

## ScrollBars

**File:** `scroll_bars.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `show_scroll_x` | `bool` | - |
| `show_scroll_y` | `bool` | - |
| `scroll_bar_x` | `ScrollBar` | - |
| `scroll_bar_y` | `ScrollBar` | - |

### Example

```rust
my_scrollbars = <ScrollBars> {
    // properties here
}
```

---

## SlidePanel

**File:** `slide_panel.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `active` | `f64` | - |
| `side` | `SlideSide` | - |

### Example

```rust
my_slidepanel = <SlidePanel> {
    // properties here
}
```

---

## Slider

**File:** `slider.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawSlider` | - |
| `axis` | `DragAxis` | DragAxis::Horizontal |
| `label_walk` | `Walk` | - |
| `label_align` | `Align` | - |
| `draw_text` | `DrawText` | - |
| `text` | `String` | - |
| `text_input` | `TextInput` | - |
| `precision` | `usize` | - |
| `min` | `f64` | - |
| `max` | `f64` | - |
| `step` | `f64` | - |
| `default` | `f64` | - |
| `bind` | `String` | - |
| `hover_actions_enabled` | `bool` | true |

### Example

```rust
my_slider = <Slider> {
    // properties here
}
```

---

## SlidesView

**File:** `slides_view.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `anim_speed` | `f64` | - |

### Example

```rust
my_slidesview = <SlidesView> {
    // properties here
}
```

---

## Splitter

**File:** `splitter.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `axis` | `SplitterAxis` | SplitterAxis::Horizontal |
| `min_vertical` | `f64` | - |
| `max_vertical` | `f64` | - |
| `min_horizontal` | `f64` | - |
| `max_horizontal` | `f64` | - |
| `draw_bg` | `DrawSplitter` | - |
| `size` | `f64` | - |
| `a` | `WidgetRef` | - |
| `b` | `WidgetRef` | - |

### Example

```rust
my_splitter = <Splitter> {
    // properties here
}
```

---

## StackNavigation

**File:** `stack_navigation.rs`

### Example

```rust
my_stacknavigation = <StackNavigation> {
    // properties here
}
```

---

## StackNavigationView

**File:** `stack_navigation.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `offset` | `f64` | - |

### Example

```rust
my_stacknavigationview = <StackNavigationView> {
    // properties here
}
```

---

## Tab

**File:** `tab.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |
| `draw_icon` | `DrawIcon` | - |
| `draw_text` | `DrawText` | - |
| `icon_walk` | `Walk` | - |
| `draw_drag` | `DrawColor` | - |
| `close_button` | `TabCloseButton` | - |
| `closeable` | `bool` | - |
| `hover` | `f32` | - |
| `active` | `f32` | - |
| `min_drag_dist` | `f64` | 10.0 |

### Example

```rust
my_tab = <Tab> {
    // properties here
}
```

---

## TabBar

**File:** `tab_bar.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `scroll_bars` | `ScrollBars` | - |
| `draw_drag` | `DrawColor` | - |
| `draw_bg` | `DrawColor` | - |
| `draw_fill` | `DrawColor` | - |

### Example

```rust
my_tabbar = <TabBar> {
    // properties here
}
```

---

## TabCloseButton

**File:** `tab_close_button.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_button` | `DrawQuad` | - |

### Example

```rust
my_tabclosebutton = <TabCloseButton> {
    // properties here
}
```

---

## TextFlow

**File:** `text_flow.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_normal` | `DrawText` | - |
| `draw_italic` | `DrawText` | - |
| `draw_bold` | `DrawText` | - |
| `draw_bold_italic` | `DrawText` | - |
| `draw_fixed` | `DrawText` | - |
| `draw_block` | `DrawFlowBlock` | - |
| `font_size` | `f32` | - |
| `font_color` | `Vec4` | - |
| `quote_layout` | `Layout` | - |
| `quote_walk` | `Walk` | - |
| `code_layout` | `Layout` | - |
| `code_walk` | `Walk` | - |
| `sep_walk` | `Walk` | - |
| `list_item_layout` | `Layout` | - |
| `list_item_walk` | `Walk` | - |
| `inline_code_padding` | `Padding` | - |
| `inline_code_margin` | `Margin` | - |

### Example

```rust
my_textflow = <TextFlow> {
    // properties here
}
```

---

## TextInput

**File:** `text_input.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawColor` | - |
| `draw_text` | `DrawText` | - |
| `draw_selection` | `DrawQuad` | - |
| `draw_cursor` | `DrawQuad` | - |
| `label_align` | `Align` | - |
| `is_password` | `bool` | - |
| `is_read_only` | `bool` | - |
| `is_numeric_only` | `bool` | - |
| `empty_text` | `String` | - |
| `text` | `String` | - |
| `blink_speed` | `f64` | 0.5 |

### Example

```rust
my_textinput = <TextInput> {
    // properties here
}
```

---

## TogglePanel

**File:** `toggle_panel.rs`

A toggable side panel that can be expanded and collapsed to a maximum and minimum size.

### Properties

| Property | Type | Default |
|----------|------|--------|
| `animator_panel_progress` | `f32` | - |
| `open_size` | `f32` | 300.0 |
| `close_size` | `f32` | 110.0 |

### Example

```rust
my_togglepanel = <TogglePanel> {
    // properties here
}
```

---

## Tooltip

**File:** `tooltip.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawQuad` | - |

### Example

```rust
my_tooltip = <Tooltip> {
    // properties here
}
```

---

## TurtleStep

**File:** `turtle_step.rs`

### Example

```rust
my_turtlestep = <TurtleStep> {
    // properties here
}
```

---

## VectorLine

**File:** `vectorline.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_ls` | `DrawLine` | - |
| `line_width` | `f64` | 15.0 |
| `color` | `Vec4` | - |
| `contained` | `bool` | true |
| `line_align` | `LineAlign` | LineAlign::Top |

### Example

```rust
my_vectorline = <VectorLine> {
    // properties here
}
```

---

## VectorSpline

**File:** `vectorspline.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_ls` | `DrawSpline` | - |
| `line_width` | `f64` | 15.0 |
| `color` | `Vec4` | - |

### Example

```rust
my_vectorspline = <VectorSpline> {
    // properties here
}
```

---

## Video

**File:** `video.rs`

UI - Playback controls - Progress/seek-to bar Widget API - Seek to timestamp - Option to restart playback manually when not looping. - Hotswap video source, `set_source(VideoDataSource)` only works if video is in Unprepared state.

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawColor` | - |
| `layout` | `Layout` | - |
| `scale` | `f64` | - |
| `source` | `VideoDataSource` | - |
| `thumbnail_source` | `Option<LiveDependency>` | - |
| `is_looping` | `bool` | false |
| `hold_to_pause` | `bool` | false |
| `autoplay` | `bool` | false |
| `mute` | `bool` | false |
| `show_thumbnail_before_playback` | `bool` | false |

### Example

```rust
my_video = <Video> {
    // properties here
}
```

---

## View

**File:** `view.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawColor` | - |
| `show_bg` | `bool` | false |
| `use_cache` | `bool` | - |
| `dpi_factor` | `Option<f64>` | - |
| `optimize` | `ViewOptimize` | - |
| `debug` | `ViewDebug` | - |
| `event_order` | `EventOrder` | - |
| `visible` | `bool` | true |
| `grab_key_focus` | `bool` | true |
| `block_signal_event` | `bool` | false |
| `cursor` | `Option<MouseCursor>` | - |
| `capture_overload` | `bool` | false |
| `scroll_bars` | `Option<LivePtr>` | - |
| `design_mode` | `bool` | false |

### Example

```rust
my_view = <View> {
    // properties here
}
```

---

## WebView

**File:** `web_view.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_bg` | `DrawWebView` | - |
| `url` | `ArcStringMut` | - |

### Example

```rust
my_webview = <WebView> {
    // properties here
}
```

---

## Window

**File:** `window.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `last_mouse_pos` | `DVec2` | - |
| `mouse_cursor_size` | `DVec2` | - |
| `demo` | `bool` | - |
| `cursor_draw_list` | `DrawList2d` | - |
| `draw_cursor` | `DrawQuad` | - |
| `debug_view` | `DebugView` | - |
| `performance_view` | `PerformanceView` | - |
| `nav_control` | `NavControl` | - |
| `window` | `WindowHandle` | - |
| `stdin_size` | `DrawColor` | - |
| `pass` | `Pass` | - |
| `hide_caption_on_fullscreen` | `bool` | - |
| `show_performance_view` | `bool` | - |
| `_default_menu` | `Menu` | - |

### Example

```rust
my_window = <Window> {
    // properties here
}
```

---

## WindowMenu

**File:** `window_menu.rs`

### Example

```rust
my_windowmenu = <WindowMenu> {
    // properties here
}
```

---

## XrHands

**File:** `xr_hands.rs`

### Properties

| Property | Type | Default |
|----------|------|--------|
| `draw_align` | `DrawCube` | - |
| `draw_test` | `DrawCube` | - |
| `draw_head` | `DrawCube` | - |
| `draw_knuckle` | `DrawCube` | - |
| `draw_controller` | `DrawCube` | - |
| `draw_bullet` | `DrawCube` | - |
| `draw_grip` | `DrawCube` | - |
| `draw_aim` | `DrawCube` | - |
| `draw_tip` | `DrawCube` | - |
| `label` | `DrawText` | - |

### Example

```rust
my_xrhands = <XrHands> {
    // properties here
}
```

---

