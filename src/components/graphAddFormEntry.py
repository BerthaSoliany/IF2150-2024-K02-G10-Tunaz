import flet as ft
from src.components.button1 import create_button1
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman
from src.controllers.datapertumbuhantanamancontroller import DataPertumbuhanTanamanController

def graph_add_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "white"
    page.theme = ft.Theme(font_family="Kantumruy-Regular")
    
    tanggal_perawatan_field = ft.CupertinoTextField(bgcolor="white", placeholder_text="Masukkan tanggal pertumbuhan di sini... (DD/MM/YYYY)", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400))
    tinggi_tanaman_field = ft.CupertinoTextField(bgcolor="white", placeholder_text="Masukkan tinggi tanaman di sini... (dalam cm)", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400))
    status_tanaman_dropdown = ft.Dropdown(bgcolor="white", width=126, hint_text="Status", hint_style=ft.TextStyle(color="black"), border_width=0, text_style=ft.TextStyle(color="black"), options=[ft.dropdown.Option("Hidup"), ft.dropdown.Option("Mati")])
    kondisi_daun_field = ft.CupertinoTextField(bgcolor="white", placeholder_text="Masukkan kondisi daun di sini...", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400))
    def on_click_add(e):
        data_pertumbuhan_controller = DataPertumbuhanTanamanController()
        data_pertumbuhan = DataPertumbuhanTanaman(status_tanaman_dropdown.value, tinggi_tanaman_field.value, tanggal_perawatan_field.value, kondisi_daun_field.value)
        data_pertumbuhan_controller.tambah_data_pertumbuhan("JERUK", 2, data_pertumbuhan) # nanti jeruk, 2 nya diganti sesuai tanamannya
        go_back(e)

    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            create_button1("Back", lambda e: page.go("/src/page/graphPage"), ft.Colors.WHITE, "#F47A6F"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Jagung 001", size=36, weight=ft.FontWeight.BOLD, color="#5F9356"),
                            ft.Image(
                            src="./img/icon1.png",  
                            width=55, 
                            height=55,  
                            fit="contain" 
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Text("Tanggal Pertumbuhan", size=20, color="black"),
                    tanggal_perawatan_field,
                    ft.Row(
                        [
                            ft.Column([
                                ft.Text("Tinggi Tanaman", size=20, color="black"),
                                tinggi_tanaman_field, 
                            ],
                            width=586,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),
                            ft.Column([
                                ft.Text("Status Tanaman", size=20, color="black"),
                                status_tanaman_dropdown,
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),  
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Text("Kondisi Daun", size=20, color="black"),
                    kondisi_daun_field, 
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="TAMBAH", on_click=on_click_add, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
                        ft.OutlinedButton(text="BATAL", on_click=go_back, width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ], 
                        alignment=ft.MainAxisAlignment.END),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=20,
            alignment=ft.alignment.center,

        ),
        width=974,
        height=564,
        color="#FDFFEA",
    )

    page.controls.clear()
    page.controls.append(
    ft.Container(
            content=form_card,
            alignment=ft.alignment.center,
            padding=20,
        )
    )
    page.update()
    return page
    # return ft.Container(
    #         content=form_card,
    #         alignment=ft.alignment.center,
    #         padding=10,
    #         bgcolor="white"
    # )