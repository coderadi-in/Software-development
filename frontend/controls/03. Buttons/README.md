# Flet `Button` &bull; PyCOD3  

Flet provides multiple button controls for user interaction, including **ElevatedButton**, **FilledButton**, **OutlinedButton**, **TextButton**, **IconButton**, and **FloatingActionButton**.  

---

## **1. Common Button Attributes**  

All button types share these core attributes:  

| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `text` | `str` | Button label text. | `""` |
| `icon` | `str` \| `ft.Icon` | Icon displayed alongside text (e.g., `ft.icons.SAVE`). | `None` |
| `on_click` | `function` | Callback when clicked. | `None` |
| `disabled` | `bool` | Disables interaction if `True`. | `False` |
| `width` | `int` \| `float` | Button width in pixels. | `None` |
| `height` | `int` \| `float` | Button height in pixels. | `None` |
| `style` | `ft.ButtonStyle` | Custom styling (color, shape, padding). | `None` |

---

## **2. Button Types**  

### **A. ElevatedButton**  
A raised button with shadow (for primary actions).  

```python
ft.ElevatedButton(
    text="Submit",
    icon="check",
    on_click=lambda e: print("Clicked!"),
)
```

### **B. FilledButton**  
A high-emphasis button (solid background).  

```python
ft.FilledButton(
    text="Confirm",
    icon="thumb_up",
)
```

### **C. FilledTonalButton**  
A medium-emphasis button (lighter fill).  

```python
ft.FilledTonalButton("Save Draft")
```

### **D. OutlinedButton**  
A button with an outline (for secondary actions).  

```python
ft.OutlinedButton(
    text="Cancel",
    icon="close",
)
```

### **E. TextButton**  
A low-emphasis button (text-only).  

```python
ft.TextButton("Learn More")
```

### **F. IconButton**  
A clickable icon (no text).  

```python
ft.IconButton(
    icon="delete",
    tooltip="Delete item",
    on_click=lambda e: print("Deleted"),
)
```

### **G. FloatingActionButton (FAB)**  
A circular button for promoted actions.  

```python
ft.FloatingActionButton(
    icon="add",
    tooltip="Create new",
)
```

---

## **3. Styling Buttons**  

### **Custom Colors & Shape**  
```python
ft.ElevatedButton(
    text="Styled Button",
    style=ft.ButtonStyle(
        color="white",
        bgcolor="blue",
        padding=20,
        shape=ft.RoundedRectangleBorder(radius=10),
    ),
)
```

### **Icon Positioning**  
```python
ft.ElevatedButton(
    text="Download",
    icon="download",
    icon_color="green",
)
```

### **Disable a Button**  
```python
ft.ElevatedButton(
    text="Disabled",
    disabled=True,
)
```

---

## **4. Event Handling**  

### **Basic Click Event**  
```python
def button_clicked(e):
    print("Button clicked!")

ft.ElevatedButton("Click Me", on_click=button_clicked)
```

### **Dynamic Button Updates**  
```python
counter = ft.Text("0")

def increment(e):
    counter.value = str(int(counter.value) + 1)
    counter.update()

page.add(
    counter,
    ft.ElevatedButton("+1", on_click=increment),
)
```

---

## **5. Full Example**  

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet Buttons Demo"

    # Button Types
    elevated_btn = ft.ElevatedButton("Elevated")
    filled_btn = ft.FilledButton("Filled")
    outlined_btn = ft.OutlinedButton("Outlined")
    text_btn = ft.TextButton("Text Button")
    icon_btn = ft.IconButton(icon="settings")
    fab = ft.FloatingActionButton(icon="add")

    # Click Event Example
    def show_snackbar(e):
        page.snack_bar = ft.SnackBar(ft.Text("Button clicked!"))
        page.snack_bar.open = True
        page.update()

    event_btn = ft.ElevatedButton(
        "Click Me",
        on_click=show_snackbar,
    )

    # Add all buttons to the page
    page.add(
        elevated_btn,
        filled_btn,
        outlined_btn,
        text_btn,
        icon_btn,
        fab,
        event_btn,
    )

ft.app(target=main)
```

---

## **6. Button Methods**  

| Method | Description |
|--------|-------------|
| `focus()` | Sets keyboard focus to the button. |
| `update()` | Applies runtime changes (e.g., after modifying `disabled`). |

---

## **References**  
- [Official Flet Buttons Docs](https://flet.dev/docs/controls/buttons/)  
- [Flet GitHub](https://github.com/flet-dev/flet)  

PyCOD3 &bull; 2025 &bull; `software development`