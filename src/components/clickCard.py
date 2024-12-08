import flet as ft

def create_click_card(page, on_click, tinggi, tanggal):
    def handle_click(e):
        on_click(e)
        page.update()  # Update the page to reflect changes
    
    def handle_hover(e):
        card.content.bgcolor = ft.Colors.GREY_200 if e.data == "true" else ft.Colors.WHITE
        card.content.update()

    card = ft.GestureDetector(
        on_tap=handle_click,
        on_hover=handle_hover,
        content=ft.Card(
            width=300,
            height=80,
            color=ft.Colors.WHITE,
            shadow_color=ft.Colors.GREY_400,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(tanggal, size=16, color="green300"),
                        ft.Text(tinggi, size=16, color="black"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=ft.Colors.WHITE,
                padding=10,
                alignment=ft.alignment.center,
            )
        )
    )

    return card