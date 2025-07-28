# Flet UI app window &bull; PyCOD3

## Overview
`Flet` is a Python framework that allows developers to build interactive multi-user web, desktop, and mobile applications without prior frontend experience. It simplifies UI development by providing a set of pre-built controls (widgets) and handling the rendering and event management.

### Key features of Flet:
- **Cross-platform** – Runs on web, desktop (Windows, macOS, Linux), and mobile (iOS, Android).
- **Simple UI development** – Uses Python for both frontend and backend logic.
- **Reactive programming** – Automatically updates the UI in response to state changes.
- **No frontend knowledge required** – No need for HTML, CSS, or JavaScript.

---

## Code documentation

### Importing Flet
```python
import flet as ft
```

- The `flet` library is imported as ft for convenience.
- This provides access to all Flet controls and functions needed to build the app.

### The main function
```python
def main(page: ft.Page):
    page.title = "Basic app window"
```

- The `main` function is the entry point for the Flet application.
- It takes a single argument, `page`, which is an instance of `ft.Page`.
    - `page` represents the main window or container for the app.
- `page.title` sets the title of the application window to "Basic app window".

### Running the app
```python
ft.app(main)
```

- `ft.app()` is used to launch the Flet application.
- It takes the `main` function as an argument, which defines the app's UI and logic.
- By default, the app opens in a native desktop window but can also be configured to run in a web browser.

---

## How the code works

### 1. Initialization:
- The Flet library is imported.
- The `main` function is defined, which sets up the basic properties of the app window.

### 2. App execution:
- `ft.app(main)` starts the Flet runtime and calls the `main` function.
- The `page` object is created and passed to `main`, allowing UI modifications.
- The window title is set to **"Basic app window"**.

### 3.Result:
- A simple desktop window opens with the specified title.
- Since no additional controls (e.g., buttons, text) are added, the window appears empty.

---

## Next steps
To extend this basic app:
- Add UI controls (e.g., `ft.Text`, `ft.Button`).
- Implement event handlers (e.g., button clicks).
- Customize the layout using `Row` and `Column` containers.

### Example
```python
def main(page: ft.Page):
    page.title = "Enhanced App"
    page.add(ft.Text("Hello, Flet!"))
    page.add(ft.ElevatedButton("Click me", on_click=lambda e: print("Button clicked!")))
```

## References
- [Flet official documentation](https://flet.dev/docs/)
- [Flet GitHub repository](https://github.com/flet-dev/flet)