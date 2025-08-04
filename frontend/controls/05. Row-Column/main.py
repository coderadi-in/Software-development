'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Layout with Rows/Columns"

    img1 = ft.Image(src="img.png", width=100, height=100, border_radius=5)
    img2 = ft.Image(src="img.png", width=100, height=100, border_radius=5)
    img3 = ft.Image(src="img.png", width=100, height=100, border_radius=5)
    img4 = ft.Image(src="img.png", width=100, height=100, border_radius=5)
    img5 = ft.Image(src="img.png", width=100, height=100, border_radius=5)

    row = ft.Column([
        img1,
        img2,
        img3,
        img4,
        img5
    ], spacing=10, alignment=ft.MainAxisAlignment.CENTER)

    page.add(row)

# ! Run the app
ft.app(main)