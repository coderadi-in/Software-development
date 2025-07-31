'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Adding text"

    inp = ft.TextField(
        label="Your name",
        hint_text="Enter your name",
        width=300,
        height=100,
        password=True,
        multiline=True,
    )

    page.add(inp)
    

# ! Run the app
ft.app(main)