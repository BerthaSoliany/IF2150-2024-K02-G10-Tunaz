import flet as ft

def create_navbar(page: ft.Page):
    page.theme = ft.Theme(font_family="Kantumruy-Regular")
    # page.bgcolor = "#FDFFEA"

    def on_home_click(e):
        page.go("/src/main")

    def on_informasi_click(e):
        page.go("/src/page/infoPage")

    def on_pertumbuhan_click(e):
        page.go("/src/page/graphPage")        

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[ft.Container(content=
                        ft.Image(
                            src="./img/logo1.png",  
                            width=170, 
                            height=95,  
                            fit="contain" 
                        ), on_click=on_home_click)
                    ],
                    alignment="start",
                ),
                ft.Row(
                    controls=[
                        ft.TextButton("Informasi Tanaman", on_click=on_informasi_click, style=ft.ButtonStyle(color="#5A3E2A", text_style=ft.TextStyle(weight="bold", size=23))),
                        ft.TextButton("Grafik Pertumbuhan", on_click=on_pertumbuhan_click, style=ft.ButtonStyle(color="#5A3E2A", text_style=ft.TextStyle(weight="bold", size=23))),
                    ],
                    alignment="end",
                ),
            ],
            alignment="spaceBetween",
            vertical_alignment="center",
        ),
        bgcolor="#FDFFEA",
        padding=4,
        margin=0
    )

""""
HOW TO USE

page.add(create_navbar(page))
"""