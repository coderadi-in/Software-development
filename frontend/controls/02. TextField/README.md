# Flet `TextField` &bull; PyCOD3

The `TextField` control in Flet allows users to input and edit text. It supports various features like validation, hint text, password masking, and event handling.  

---

## **Importing the `TextField` Control**  
```python
import flet as ft

text_field = ft.TextField()
```

---

## **Basic Attributes**  

| Attribute | Type | Description | Default |
|-----------|------|-------------|---------|
| `value` | `str` | The current text in the field. | `""` (empty) |
| `label` | `str` | A floating label above the field. | `None` |
| `hint_text` | `str` | Placeholder text when the field is empty. | `None` |
| `helper_text` | `str` | Help text displayed below the field. | `None` |
| `error_text` | `str` | Error text displayed when validation fails. | `None` |
| `prefix_text` | `str` | Text displayed before the input (e.g., `"$"`). | `None` |
| `suffix_text` | `str` | Text displayed after the input (e.g., `".com"`). | `None` |
| `icon` | `ft.Icon` | An icon displayed at the start of the field. | `None` |
| `bgcolor` | `str` | Background color of the field. | `None` |
| `color` | `str` | Text color. | `None` (theme default) |
| `border` | `ft.InputBorder` | Border style (`OUTLINE`, `UNDERLINE`, `NONE`). | `OUTLINE` |
| `border_radius` | `int` \| `float` | Border corner radius. | `None` |
| `border_color` | `str` | Border color when inactive. | `None` |
| `focused_border_color` | `str` | Border color when focused. | `None` |
| `text_size` | `int` \| `float` | Font size of the input text. | `None` |
| `text_align` | `ft.TextAlign` | Text alignment (`LEFT`, `CENTER`, `RIGHT`). | `LEFT` |
| `multiline` | `bool` | Allows multiple lines of input. | `False` |
| `min_lines` | `int` | Minimum lines (for multiline). | `None` |
| `max_lines` | `int` | Maximum lines (for multiline). | `None` |
| `max_length` | `int` | Maximum allowed characters. | `None` |
| `password` | `bool` | Masks input (for passwords). | `False` |
| `can_reveal_password` | `bool` | Shows a "reveal" button for passwords. | `False` |
| `read_only` | `bool` | Makes the field non-editable. | `False` |
| `shift_enter` | `bool` | Allows new lines with `Shift+Enter`. | `False` |
| `keyboard_type` | `ft.KeyboardType` | Optimizes keyboard for input type (`TEXT`, `NUMBER`, `EMAIL`, etc.). | `TEXT` |
| `capitalization` | `ft.TextCapitalization` | Auto-capitalization (`NONE`, `WORDS`, `SENTENCES`, `CHARACTERS`). | `NONE` |
| `autocorrect` | `bool` | Enables/disables auto-correction. | `True` |
| `content_padding` | `int` \| `tuple` | Padding inside the field (e.g., `10` or `(5, 10)`). | `None` |
| `on_change` | `function` | Called when text changes. | `None` |
| `on_submit` | `function` | Called when `Enter` is pressed. | `None` |
| `on_focus` | `function` | Called when field gains focus. | `None` |
| `on_blur` | `function` | Called when field loses focus. | `None` |

---

## **Methods**  

| Method | Description |
|--------|-------------|
| `focus()` | Sets focus to the field. |
| `update()` | Refreshes the field to apply changes. |
| `clear()` | Clears the input text. |

---

## **Styling & Behavior**  

### **1. Basic TextField with Label & Hint**  
```python
ft.TextField(
    label="Username",
    hint_text="Enter your username",
)
```

### **2. Password Field**  
```python
ft.TextField(
    label="Password",
    password=True,
    can_reveal_password=True,
)
```

### **3. Multiline Input**  
```python
ft.TextField(
    label="Description",
    multiline=True,
    min_lines=3,
    max_lines=5,
)
```

### **4. Input Validation**  
```python
def validate_email(e):
    if "@" not in email_field.value:
        email_field.error_text = "Invalid email!"
    else:
        email_field.error_text = None
    email_field.update()

email_field = ft.TextField(
    label="Email",
    on_blur=validate_email,
)
```

### **5. Numeric Input**  
```python
ft.TextField(
    label="Age",
    keyboard_type=ft.KeyboardType.NUMBER,
)
```

### **6. Custom Styling (Border & Padding)**  
```python
ft.TextField(
    label="Custom Field",
    border_color="blue",
    focused_border_color="purple",
    border_radius=10,
    content_padding=10,
)
```

---

## **Event Handling**  

### **1. `on_change` Example**  
```python
def text_changed(e):
    print(f"Text changed to: {e.control.value}")

ft.TextField(
    on_change=text_changed,
)
```

### **2. `on_submit` Example**  
```python
def handle_submit(e):
    print(f"Submitted: {e.control.value}")

ft.TextField(
    on_submit=handle_submit,
)
```

### **3. `focus()` & `clear()` Example**  
```python
name_field = ft.TextField(label="Name")

def clear_and_focus(e):
    name_field.clear()
    name_field.focus()

page.add(
    name_field,
    ft.ElevatedButton("Clear & Focus", on_click=clear_and_focus),
)
```

---

## **Full Example**  

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet TextField Example"
    
    # Basic TextField
    name_field = ft.TextField(
        label="Full Name",
        hint_text="Enter your name",
        width=300,
    )
    
    # Password Field
    password_field = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
    )
    
    # Multiline Input
    bio_field = ft.TextField(
        label="Bio",
        multiline=True,
        min_lines=3,
    )
    
    # Numeric Input
    age_field = ft.TextField(
        label="Age",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    
    # Submit Button
    def submit_form(e):
        print(f"Name: {name_field.value}")
        print(f"Age: {age_field.value}")
        page.snack_bar = ft.SnackBar(ft.Text("Form submitted!"))
        page.snack_bar.open = True
        page.update()
    
    submit_btn = ft.ElevatedButton("Submit", on_click=submit_form)
    
    # Add all controls to the page
    page.add(
        name_field,
        password_field,
        bio_field,
        age_field,
        submit_btn,
    )

ft.app(target=main)
```

---

## **References**  
- [Official Flet TextField Docs](https://flet.dev/docs/controls/textfield/)  
- [Flet GitHub](https://github.com/flet-dev/flet)  

PyCODE &bull; 2025 &bull; `software development`