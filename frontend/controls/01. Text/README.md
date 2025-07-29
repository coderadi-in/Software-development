# Flet `Text` Control Documentation  

The `Text` control in Flet is used to display a piece of text in your application. It supports styling, formatting, and interactive features such as hyperlinks and selections.  

---

## **Importing the `Text` Control**  
```python
import flet as ft

text = ft.Text("Hello, Flet!")
```

---

## **Basic Attributes**  

| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `value` | `str` | The text string to display. | `""` (empty) |
| `color` | `str` | Text color (e.g., `"red"`, `"#00FF00"`). | `None` (default theme) |
| `size` | `int` \| `float` | Font size in logical pixels. | `14` |
| `weight` | `ft.FontWeight` | Font weight (e.g., `ft.FontWeight.BOLD`). | `None` |
| `font_family` | `str` | Font family (e.g., `"Arial"`, `"Roboto"`). | `None` |
| `style` | `ft.TextStyle` | Additional styling (e.g., `italic`, `underline`). | `None` |
| `text_align` | `ft.TextAlign` | Horizontal alignment (`LEFT`, `CENTER`, `RIGHT`, `JUSTIFY`). | `LEFT` |
| `max_lines` | `int` | Maximum number of lines before truncation. | `None` (unlimited) |
| `overflow` | `ft.TextOverflow` | Behavior when text overflows (`CLIP`, `ELLIPSIS`, `FADE`). | `ELLIPSIS` |
| `selectable` | `bool` | Whether the text can be selected by the user. | `False` |
| `spans` | `List[ft.TextSpan]` | Rich text with multiple styles/links. | `None` |
| `no_wrap` | `bool` | Prevents text from wrapping to the next line. | `False` |
| `semantics_label` | `str` | Accessibility label for screen readers. | `None` |

---

## **Styling & Formatting**  

### **1. Changing Font Weight**  
```python
ft.Text("Bold Text", weight=ft.FontWeight.BOLD)
```  
Supported weights:  
- `FontWeight.NORMAL`  
- `FontWeight.BOLD`  
- `FontWeight.W_100` to `FontWeight.W_900`  

### **2. Italics & Underline**  
```python
ft.Text("Italic & Underlined", style=ft.TextStyle(italic=True, decoration=ft.TextDecoration.UNDERLINE))
```  

### **3. Text Color & Background**  
```python
ft.Text("Red Text", color="red")
ft.Text("Highlighted", bgcolor="yellow")
```  

### **4. Alignment**  
```python
ft.Text("Centered Text", text_align=ft.TextAlign.CENTER)
```  

### **5. Max Lines & Overflow**  
```python
ft.Text(
    "A very long text that will be truncated...",
    max_lines=1,
    overflow=ft.TextOverflow.ELLIPSIS,
)
```  

---

## **Interactive Text Features**  

### **1. Selectable Text**  
```python
ft.Text("Select me!", selectable=True)
```  

### **2. Clickable Links (TextSpan)**  
```python
ft.Text(spans=[
    ft.TextSpan("Visit Google", url="https://google.com", style=ft.TextStyle(color="blue")),
])
```  

### **3. Rich Text (Multiple Styles in One Line)**  
```python
ft.Text(spans=[
    ft.TextSpan("Normal "),
    ft.TextSpan("Bold", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
    ft.TextSpan(" & Red", style=ft.TextStyle(color="red")),
])
```  

---

## **Methods**  

| Method | Description |
|--------|-------------|
| `update()` | Refreshes the text control to apply changes. |  

### **Example: Updating Text Dynamically**  
```python
text = ft.Text("Initial Text")

def update_text(e):
    text.value = "Updated Text!"
    text.update()

page.add(text, ft.ElevatedButton("Update Text", on_click=update_text))
```  

---

## **Full Example**  

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet Text Example"
    
    # Basic Text
    basic_text = ft.Text("Hello, Flet!", size=20, color="blue")
    
    # Styled Text
    styled_text = ft.Text(
        "Styled Text",
        weight=ft.FontWeight.BOLD,
        style=ft.TextStyle(italic=True, decoration=ft.TextDecoration.UNDERLINE),
        color="green",
    )
    
    # Rich Text with Spans
    rich_text = ft.Text(spans=[
        ft.TextSpan("Click "),
        ft.TextSpan("here", style=ft.TextStyle(color="blue", decoration=ft.TextDecoration.UNDERLINE)),
        ft.TextSpan(" to visit Flet docs", url="https://flet.dev"),
    ])
    
    # Adding to the page
    page.add(basic_text, styled_text, rich_text)

ft.app(target=main)
```  

---

## **References**  
- [Official Flet Text Documentation](https://flet.dev/docs/controls/text/)  
- [Flet GitHub](https://github.com/flet-dev/flet)  

PyCOD3 &bull; 2025 &bull; `software development`