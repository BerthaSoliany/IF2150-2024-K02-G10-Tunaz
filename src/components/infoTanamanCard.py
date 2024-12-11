import flet as ft

def create_info_tanaman_card(page: ft.Page, on_click=None):
    def handle_click(e):
        if on_click:
            on_click(e)
        # page.update()  # Update the page to reflect changes

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            "Jagung 002",
                            size=24,
                            weight="bold",
                            color="#5F9356",
                        ),
                        ft.Image(
                            src="./img/card_icon1.png",
                            width=40,
                            height=40,
                            fit="contain",
                        ),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Text(
                    "Disiram dengan pupuk quality extra pulen yang tiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadak mengandung red 40. Penyiraman dilakukan dengan spray bottle atau selang dengan ukuran nozzle 0,1 mmjbdasdhvfluaevfluasdv",
                    size=16,
                    color="black",
                    # style=ft.TextStyle(font_family="Verdana"),
                    overflow=ft.TextOverflow.ELLIPSIS,
                    max_lines=5
                ),
                ft.Row(
                    controls=[
                        ft.Image(
                            src="./img/plant_age.png",
                            width=20,
                            height=20,
                            fit="contain",
                        ),
                        ft.Text(
                            "1 bulan",
                            size=16,
                            color="#8C8C8C",
                            weight="bold",
                            # style=ft.TextStyle(font_family="Verdana"),
                        ),
                    ],
                    alignment="start",
                ),
            ],
            spacing=10,
        ),
        bgcolor="#FDFFEA",
        padding=20,
        border_radius=12,
        width=None, 
        height=None, 
        border=ft.border.all(1, "#D7D7D7"),
        expand=True,  # how to make width n height sesuai window size tapi kalo dia ga pas 3 ga expand...?
        on_click=handle_click,
    )
