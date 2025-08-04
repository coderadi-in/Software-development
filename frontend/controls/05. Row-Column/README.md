# Flet `Row` & `Column` &bull; PyCOD3

The `Row` and `Column` controls are Flet's fundamental layout elements for arranging child controls horizontally (`Row`) and vertically (`Column`).

## Importing Row and Column
```python
import flet as ft

row = ft.Row()
column = ft.Column()
```

## Common Attributes (Shared by Both)

| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `controls` | `List[Control]` | Child elements to arrange | `[]` |
| `alignment` | `MainAxisAlignment` | Primary axis alignment | `START` |
| `spacing` | `int`/`float` | Space between children | `None` |
| `expand` | `bool`/`int` | Expand to fill available space | `False` |
| `scroll` | `ScrollMode` | Scroll behavior (`AUTO`, `ALWAYS`, `HIDDEN`) | `None` |
| `wrap` | `bool` | Wrap children to new line/column | `False` |
| `vertical_alignment` | `CrossAxisAlignment` | Cross-axis alignment | `START` |
| `horizontal_alignment` | `CrossAxisAlignment` | Cross-axis alignment | `START` |
| `clip_behavior` | `ClipBehavior` | Content clipping behavior | `NONE` |

## Row-Specific Attributes

| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `vertical_alignment` | `CrossAxisAlignment` | Vertical alignment of children | `START` |

## Column-Specific Attributes

| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `horizontal_alignment` | `CrossAxisAlignment` | Horizontal alignment of children | `START` |

## Alignment Options

### Main Axis Alignment (for both Row and Column)
- `START` - Pack children at the start
- `END` - Pack children at the end
- `CENTER` - Center children
- `SPACE_BETWEEN` - Equal space between children
- `SPACE_AROUND` - Equal space around children
- `SPACE_EVENLY` - Equal space including edges

### Cross Axis Alignment
- `START` - Align to start (left/top)
- `END` - Align to end (right/bottom)
- `CENTER` - Center along cross axis
- `STRETCH` - Stretch to fill cross axis
- `BASELINE` - Align by text baseline (Row only)

## Basic Examples

### 1. Simple Row
```python
ft.Row(
    controls=[
        ft.Text("Item 1"),
        ft.Text("Item 2"),
        ft.Text("Item 3")
    ],
    spacing=10,
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
)
```

### 2. Simple Column
```python
ft.Column(
    controls=[
        ft.Text("Top"),
        ft.Text("Middle"),
        ft.Text("Bottom")
    ],
    spacing=20,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)
```

## Advanced Layout Techniques

### 1. Mixed Sizing
```python
ft.Row(
    controls=[
        ft.Container(width=50, height=50, bgcolor="red"),  # Fixed size
        ft.Container(expand=True, height=100, bgcolor="blue"),  # Expands
        ft.Container(width=100, height=30, bgcolor="green")  # Fixed size
    ],
    height=200
)
```

### 2. Scrolling
```python
ft.Column(
    controls=[ft.Text(f"Item {i}") for i in range(50)],
    scroll=ft.ScrollMode.AUTO,
    height=300
)
```

### 3. Wrapping Content
```python
ft.Row(
    controls=[ft.Container(width=100, height=100, bgcolor=c) for c in ["red", "blue", "green", "yellow"]],
    wrap=True,
    spacing=10,
    run_spacing=10  # Vertical space between wrapped lines
)
```

### 4. Nested Layouts
```python
ft.Column(
    controls=[
        ft.Row(
            controls=[ft.Text("Header 1"), ft.Text("Header 2")],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        ft.Row(
            controls=[ft.Text("Content"), ft.Text("Sidebar")],
            vertical_alignment=ft.CrossAxisAlignment.START
        )
    ]
)
```

## Responsive Design Patterns

### 1. Responsive Row-to-Column
```python
def layout_func(page):
    if page.width < 600:  # Mobile view
        return ft.Column(controls=[content, sidebar])
    else:  # Desktop view
        return ft.Row(controls=[content, sidebar], vertical_alignment=ft.CrossAxisAlignment.START)
```

### 2. Expanding Sections
```python
ft.Column(
    controls=[
        ft.Container(content=ft.Text("Header"), height=50),
        ft.Row(
            controls=[
                ft.Container(content=ft.Text("Nav"), width=100),
                ft.Container(content=ft.Text("Main"), expand=True)
            ],
            expand=True
        ),
        ft.Container(content=ft.Text("Footer"), height=30)
    ],
    expand=True
)
```

## Performance Considerations

### 1. Efficient Scrolling
```python
# Good for long lists
ft.Column(
    controls=[ft.ListTile(title=ft.Text(f"Item {i}")) for i in range(1000)],
    scroll=ft.ScrollMode.ALWAYS,
    height=400
)

# Better alternative for very long lists:
ft.ListView(controls=[...], expand=True)
```

### 2. Layout Optimization
```python
# Avoid:
ft.Column(controls=[ft.Row(controls=[...]), ft.Row(controls=[...])])

# Prefer:
ft.Column(controls=[
    ft.Row(controls=[...], spacing=10),
    ft.Row(controls=[...], spacing=10)
])
```

## Full Example

```python
import flet as ft

def main(page: ft.Page):
    # Responsive layout example
    def build_layout():
        content = ft.Container(content=ft.Text("Main Content"), expand=True, padding=10)
        sidebar = ft.Container(content=ft.Text("Sidebar"), width=200, padding=10)
        
        if page.width < 600:
            return ft.Column(controls=[content, sidebar])
        else:
            return ft.Row(
                controls=[sidebar, content],
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=10
            )

    page.on_resize = lambda e: page.update()
    
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Responsive Layout Demo", size=20),
                    build_layout()
                ],
                expand=True
            ),
            padding=10
        )
    )

ft.app(target=main)
```

## Methods

| Method | Description |
|--------|-------------|
| `update()` | Refresh the layout |
| `clean()` | Remove all children |
| `insert(index, control)` | Insert control at position |
| `remove(control)` | Remove specific control |
| `replace(old, new)` | Swap controls |

## Common Patterns

### 1. Dynamic Content Updates
```python
column = ft.Column()

def add_item(e):
    column.controls.append(ft.Text(f"New Item {len(column.controls)}"))
    column.update()

page.add(
    column,
    ft.ElevatedButton("Add Item", on_click=add_item)
)
```

### 2. Conditional Layouts
```python
ft.Column(
    controls=[
        ft.Text("Status:"),
        ft.Row(
            controls=[
                ft.Icon(ft.icons.CHECK if success else ft.icons.ERROR),
                ft.Text("Success" if success else "Error")
            ]
        )
    ]
)
```

## References
- [Official Row Documentation](https://flet.dev/docs/controls/row)
- [Official Column Documentation](https://flet.dev/docs/controls/column)
- [Flet GitHub Repository](https://github.com/flet-dev/flet)

PyCOD3 &bull; 2025 &bull; `software development`