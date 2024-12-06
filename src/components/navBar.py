import flet as ft

def create_navbar(page: ft.Page):
    # ini fungsi untuk route navbar. blm fiks masih bisa diubah
    def on_home_click(e):
        page.go("/home")

    def on_informasi_click(e):
        page.go("/informasi")

    def on_pertumbuhan_click(e):
        page.go("/pertumbuhan")

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Image(
                            src="./img/logo1.png",  
                            width=90, 
                            height=90,  
                            fit="contain" 
                        ),
                    ],
                    alignment="start",
                ),
                ft.Row(
                    controls=[
                        ft.TextButton("Home", on_click=on_home_click, style=ft.ButtonStyle(color=ft.colors.BROWN_700, text_style=ft.TextStyle(weight="bold", size=18))),
                        ft.TextButton("Informasi Tanaman", on_click=on_informasi_click, style=ft.ButtonStyle(color=ft.colors.BROWN_700, text_style=ft.TextStyle(weight="bold", size=18))),
                        ft.TextButton("Grafik Pertumbuhan", on_click=on_pertumbuhan_click, style=ft.ButtonStyle(color=ft.colors.BROWN_700, text_style=ft.TextStyle(weight="bold", size=18))),
                    ],
                    alignment="end",
                ),
            ],
            alignment="spaceBetween",
            vertical_alignment="center",
        ),
        bgcolor=ft.colors.YELLOW_100,
        padding=5,
        margin=0
    )

""""
HOW TO USE

page.add(create_navbar(page))
"""