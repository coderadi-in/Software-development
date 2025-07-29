'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Adding text"

    txt = ft.Text(
        value="This is a text.",
        size=32,
        color="#FFFDD0",
        weight="bold",
        italic=True
    )

    page.add(txt)

# ! Run the app
ft.app(main)