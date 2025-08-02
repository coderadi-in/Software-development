# Flet `Container` &bull; PyCOD3

The `Container` control is one of Flet's most versatile layout elements, acting as a wrapper that can hold a single child while providing styling options like padding, borders, backgrounds, and animations.

## Importing the Container
```python
import flet as ft

container = ft.Container()
```

## Basic Attributes

| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `content` | `Control` | The single child widget contained within | `None` |
| `padding` | `int`/`tuple` | Space between content and borders | `None` |
| `margin` | `int`/`tuple` | Space outside container borders | `None` |
| `bgcolor` | `str` | Background color (hex/RGB/name) | `None` |
| `gradient` | `Gradient` | Background gradient | `None` |
| `border` | `Border` | Border styling | `None` |
| `border_radius` | `int`/`float`/`BorderRadius` | Corner rounding | `None` |
| `width` | `int`/`float` | Container width | `None` |
| `height` | `int`/`float` | Container height | `None` |
| `alignment` | `Alignment` | Content positioning | `None` |
| `animate` | `bool`/`int` | Animation duration (ms) | `None` |
| `blur` | `int`/`tuple` | Blur effect | `None` |
| `shadow` | `BoxShadow` | Shadow effect | `None` |
| `clip_behavior` | `ClipBehavior` | Content clipping | `None` |
| `ink` | `bool` | Ripple effect | `False` |
| `url` | `str` | Hyperlink destination | `None` |
| `on_click` | `function` | Click handler | `None` |

## Styling Options

### 1. Basic Styling
```python
ft.Container(
    content=ft.Text("Hello"),
    padding=20,
    bgcolor="blue",
    border_radius=10,
    width=200,
    height=100,
)
```

### 2. Advanced Borders
```python
ft.Container(
    border=ft.border.all(2, "red"),
    border_radius=ft.border_radius.only(top_left=10, bottom_right=10)
)
```

### 3. Gradients
```python
ft.Container(
    gradient=ft.LinearGradient(
        begin=ft.alignment.top_left,
        end=ft.alignment.bottom_right,
        colors=["blue", "purple"]
    )
)
```

### 4. Shadows
```python
ft.Container(
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLUE_300,
        offset=ft.Offset(5, 5)
)
```

### 5. Animation
```python
ft.Container(
    animate=300,  # 300ms animation
    on_hover=lambda e: setattr(e.control, "bgcolor", "red" if e.data == "true" else "blue")
)
```

## Layout Behavior

### 1. Content Alignment
```python
ft.Container(
    alignment=ft.alignment.center,
    content=ft.Text("Centered")
)
```

### 2. Padding Variations
```python
# Uniform padding
ft.Container(padding=10)

# Asymmetric padding
ft.Container(padding=ft.padding.only(left=20, top=10))

# Edge-specific padding
ft.Container(padding=ft.padding.symmetric(vertical=10, horizontal=20))
```

### 3. Constrained vs Unconstrained
```python
# Expands to fill parent
ft.Container(expand=True)

# Fixed size
ft.Container(width=100, height=100)

# Percentage of parent
ft.Container(width=0.5, height=0.5)  # 50% of parent
```

## Interactive Features

### 1. Click Handling
```python
ft.Container(
    content=ft.Text("Clickable"),
    on_click=lambda e: print("Clicked!"),
    ink=True  # Adds ripple effect
)
```

### 2. Hover Effects
```python
def on_hover(e):
    e.control.bgcolor = "blue" if e.data == "true" else "green"
    e.control.update()

ft.Container(
    on_hover=on_hover
)
```

## Advanced Usage

### 1. Nested Containers
```python
ft.Container(
    content=ft.Container(
        content=ft.Text("Nested"),
        bgcolor="white",
        padding=10
    ),
    bgcolor="black",
    padding=20
)
```

### 2. Clip Behavior
```python
ft.Container(
    clip_behavior=ft.ClipBehavior.HARD_EDGE,
    border_radius=20,
    content=ft.Image(src="large_image.png")
)
```

### 3. Blur Effects
```python
ft.Container(
    blur=ft.Blur(10, 10, ft.BlurTileMode.MIRROR)
)
```

## Full Example

```python
import flet as ft

def main(page: ft.Page):
    # Animated container
    def animate_container(e):
        c.width = 300 if c.width == 200 else 200
        c.bgcolor = "purple" if c.bgcolor == "blue" else "blue"
        c.update()

    c = ft.Container(
        width=200,
        height=200,
        bgcolor="blue",
        border_radius=10,
        animate=ft.animation.Animation(500, "bounceOut"),
        on_click=animate_container
    )

    # Gradient container with shadow
    gradient_container = ft.Container(
        width=150,
        height=150,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.PINK, ft.colors.PURPLE]
        ),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.colors.PURPLE_300,
            offset=ft.Offset(5, 5)
    )

    page.add(
        ft.Column([
            ft.Text("Interactive Container:"),
            c,
            ft.Text("Styled Container:"),
            gradient_container
        ])
    )

ft.app(target=main)
```

## Methods

| Method | Description |
|--------|-------------|
| `update()` | Applies property changes |
| `animate_opacity()` | Fades container in/out |

## Performance Notes
- Avoid excessive nesting of containers
- Use `animate` judiciously for smooth performance
- Prefer `border_radius` over complex clipping for better rendering

## References
- [Official Container Documentation](https://flet.dev/docs/controls/container/)
- [Flet GitHub Repository](https://github.com/flet-dev/flet)

PyCOD3 &bull; 2025 &bull; `software development`