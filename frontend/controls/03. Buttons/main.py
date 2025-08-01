'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Flet buttons"

    def func(e):
        btn.text = "Clicked!"
        btn.update()

    btn = ft.ElevatedButton(
        icon=ft.Icons.ADS_CLICK,
        text="click me",
        on_click=func
    )

    page.add(btn)

# ! Run the app
ft.app(main)