import flet as ft

def main(page: ft.Page):
    page.title = "Container"

    container = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Image(
                    src="img.png",
                    border_radius=50,
                    width=50,
                    height=50
                ),
                ft.Text(
                    value="BMW M4",
                    size=36,
                    color="#FFFFFF"
                )
            ]),

            ft.Text(
                value="High-Performance M TwinPower Turbo inline 6-cylinder petrol engine. The M4 Competition Coupé with M xDrive guarantees maximum driving dynamics.",
                size=16,
                color="#FFFFFF"
            ),

            ft.Row([
                ft.TextButton(text="Details"),
                ft.FilledButton(text="Buy now")
            ], alignment=ft.MainAxisAlignment.END)
        ]),
        width=400,
        padding=20,
        border_radius=20,
        bgcolor="#2C2C31"
    )

    page.add(container)

ft.app(main)