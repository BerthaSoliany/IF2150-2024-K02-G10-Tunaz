import flet as ft

def create_click_card(page, on_click, tinggi, tanggal):
    def handle_click(e):
        on_click(e)
        page.update()  # Update the page to reflect changes
    
    def handle_hover(e):
        card.content.color = ft.Colors.GREY_200 if e.data == "true" else ft.Colors.WHITE
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
                        ft.Text(tanggal, size=16, color="#5F9356"),
                        ft.Text(tinggi, size=15, color="black"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                bgcolor=ft.Colors.WHITE,
                padding=10,
                alignment=ft.alignment.center,
                border_radius=10,
                border=ft.border.all(1, ft.Colors.GREY_200)
            )
        )
    )

    return card


def create_click_card2(page, on_click, waktu, perawatan_jenis_index, kebutuhan_perawatan):
    def handle_click(e):
        on_click(e)
        page.update()  # Update the page to reflect changes
    
    def handle_hover(e):
        card.content.color = ft.Colors.GREY_200 if e.data == "true" else ft.Colors.WHITE
        card.content.update()

    card = ft.GestureDetector(
        on_tap=handle_click,
        on_hover=handle_hover,
        content=ft.Card(
            width=342,
            height=100,
            color=ft.Colors.WHITE,
            shadow_color=ft.Colors.GREY_400,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(waktu, size=16, color="black"),
                        ft.Text(perawatan_jenis_index, size=20, color="#5F9356", weight=ft.FontWeight.BOLD),
                        ft.Text(kebutuhan_perawatan, size=16, color="grey600", overflow=ft.TextOverflow.ELLIPSIS),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    spacing=2,
                ),
                bgcolor=ft.Colors.WHITE,
                padding=5,
                alignment=ft.Alignment(-1, 0),
                border_radius=10,
                border=ft.border.all(1, ft.Colors.GREY_200)
            )
        )
    )

    return card