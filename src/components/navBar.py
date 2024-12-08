import flet as ft

def create_navbar(page: ft.Page):
    page.theme = ft.Theme(font_family="Kantumruy-Regular")

    def on_home_click(e):
        page.go("/src/page/homePage")

    def on_informasi_click(e):
        page.go("/informasi")

    def on_pertumbuhan_click(e):
        page.go("/src/page/graphPage")        

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Image(
                            src="/img/logo1.png",  
                            width=90, 
                            height=90,  
                            fit="contain" 
                        ),
                    ],
                    alignment="start",
                ),
                ft.Row(
                    controls=[
                        ft.TextButton("Home", on_click=on_home_click, style=ft.ButtonStyle(color="#5A3E2A", text_style=ft.TextStyle(weight="bold", size=18))),
                        ft.TextButton("Informasi Tanaman", on_click=on_informasi_click, style=ft.ButtonStyle(color="#5A3E2A", text_style=ft.TextStyle(weight="bold", size=18))),
                        ft.TextButton("Grafik Pertumbuhan", on_click=on_pertumbuhan_click, style=ft.ButtonStyle(color="#5A3E2A", text_style=ft.TextStyle(weight="bold", size=18))),
                    ],
                    alignment="end",
                ),
            ],
            alignment="spaceBetween",
            vertical_alignment="center",
        ),
        bgcolor="#FDFFEA",
        padding=5,
        margin=0
    )

""""
HOW TO USE

page.add(create_navbar(page))
"""