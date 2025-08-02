'''PyCOD3 | @_py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "UI layout with Container"

    c = ft.Container(
        content=ft.Text("text"),
        padding=20,
        bgcolor="#4C8EFF",
        border_radius=10
    )

    page.add(c)

# ! Run the app
ft.app(main)