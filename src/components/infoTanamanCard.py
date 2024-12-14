import flet as ft
from src.controllers.tanaman import Tanaman
from datetime import date
def create_info_tanaman_card(page: ft.Page, x: Tanaman, on_click=None):
    def handle_click(e):
        if on_click:
            page.session.set("Tanaman", x)
            on_click(e)
        # page.update()  # Update the page to reflect changes

    def to_date(dt_date):
        yy, mm, dd = map(int, dt_date.split('-'))
        return date(yy, mm, dd)
    
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            x.get_jenis() + " " + str(x.get_index()),
                            size=24,
                            weight="bold",
                            color="#5F9356",
                            overflow=ft.TextOverflow.ELLIPSIS,
                            width=325,
                        ),
                        ft.Image(
                            src="./img/" + x.get_icon() +".png",
                            width=40,
                            height=40,
                            fit="contain",
                        ),
                    ],
                    alignment="spaceBetween",
                ),
                ft.Text(
                    x.get_data_informasi_tanaman().get_kebutuhan_perawatan(),
                    size=16,
                    color="black",
                    # style=ft.TextStyle(font_family="Verdana"),
                    overflow=ft.TextOverflow.ELLIPSIS,
                    max_lines=4
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
                            str((date.today() - to_date(x.get_data_informasi_tanaman().get_waktu_tanam())).days) + " hari",
                            size=16,
                            color="#8C8C8C",
                            weight="bold",
                            # style=ft.TextStyle(font_family="Verdana"),
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                    ],
                    alignment="start",
                ),
            ],
            spacing=10,
            alignment="spaceBetween",
        ),
        bgcolor="#FDFFEA",
        padding=20,
        border_radius=12,
        width=360, 
        height=220, 
        border=ft.border.all(1, "#D7D7D7"),
        expand=True,  # how to make width n height sesuai window size tapi kalo dia ga pas 3 ga expand...?
        on_click=handle_click,
    )
