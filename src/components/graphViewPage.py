import flet as ft
from datetime import datetime, timedelta, date
from src.components.button1 import create_button1
from src.components.validasi import validasi
from src.controllers.datapertumbuhantanamancontroller import DataPertumbuhanTanamanController
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman
from src.controllers.tanaman import Tanaman
from src.controllers.grafikpertumbuhan import GrafikPertumbuhan

def graph_view_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    dialog = validasi(page, "/src/page/graphPage")
    def show_dialog(e):
        page.session.set("action", "hapus_data_pertumbuhan")
        page.open(dialog)

    def to_date(dt_date):
        yy, mm, dd = map(int, dt_date.split('-'))
        return date(yy, mm, dd)

    def to_date2(dt_date):
        dd, mm, yy = map(int, dt_date.split('/'))
        return date(yy, mm, dd)
        
    if(page.session.get("data_pertumbuhan_tanaman") == None):
        graph = GrafikPertumbuhan()
        # new_data_points, data_tanggal = graph.tinggi_terhadap_waktu(Tanaman(jenis_tanaman=page.session.get("jenis_tanaman"), index_tanaman=page.session.get("index_tanaman"), icon_tanaman=None, data_informasi_tanaman=None, data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None))
        data_pertumbuhan_tanaman = DataPertumbuhanTanaman(status_tanaman=None, kondisi_daun=None, tanggal_catatan=None, tinggi_tanaman=page.session.get("tinggi_tanaman"))
        data_pertumbuhan_tanaman_controller = DataPertumbuhanTanamanController()
        # data_pertumbuhan_tanaman.set_tanggal_catatan(to_date(data_tanggal[0]) + timedelta(days=page.session.get("tanggal_catatan")))
        # data_pertumbuhan_tanaman.set_tanggal_catatan(data_pertumbuhan_tanaman.get_tanggal_catatan().strftime('%Y-%m-%d'))
        data_pertumbuhan_tanaman.set_tanggal_catatan(page.session.get("tanggal_catatan"))
        data_pertumbuhan_tanaman = data_pertumbuhan_tanaman_controller.get_data_pertumbuhan(page.session.get("jenis_tanaman"), page.session.get("index_tanaman"), data_pertumbuhan_tanaman)
        page.session.set("data_pertumbuhan_tanaman", data_pertumbuhan_tanaman)
        page.session.set("tinggi_tanaman", None)
        page.session.set("tanggal_catatan", None)

    data_pertumbuhan_tanaman = page.session.get("data_pertumbuhan_tanaman")
    tanggal_pertumbuhan_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text=datetime.strptime(data_pertumbuhan_tanaman.get_tanggal_catatan(),"%Y-%m-%d").strftime("%d/%m/%Y"), placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    tinggi_tanaman_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text=data_pertumbuhan_tanaman.get_tinggi_tanaman(), placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    status_tanaman_dropdown = ft.Dropdown(icon_enabled_color="black", border_radius=5, border_color="black",bgcolor="white", width=126, hint_content=ft.Text(value=data_pertumbuhan_tanaman.get_status_tanaman(), color="grey400", size="16"), border_width=1, text_style=ft.TextStyle(color="black"), options=[ft.dropdown.Option("Hidup"), ft.dropdown.Option("Mati")], disabled=True)
    kondisi_daun_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text=data_pertumbuhan_tanaman.get_kondisi_daun(), placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    jenis_index = page.session.get("jenis_tanaman") + " " + page.session.get("index_tanaman") # nanti diganti sesuai tanamannya
    icon = page.session.get("icon_tanaman") # nanti diganti sesuai icon tanamannya

    def on_click_back_to_graph_page(e):
        page.session.set("data_pertumbuhan_tanaman", None)
        # page.session.set("jenis_tanaman", None)
        # page.session.set("index_tanaman", None)
        page.go("/src/page/graphPage")

    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(icon="arrow_back", on_click=on_click_back_to_graph_page, icon_color="#5F9356"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(jenis_index, size=36, weight=ft.FontWeight.BOLD, color="#5F9356"), # Change this to the name of the plant
                            ft.Image(
                            src="./img/"+icon+".png",  
                            width=55, 
                            height=55,  
                            fit="contain" 
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Text("Tanggal Pertumbuhan", size=20, color="black"),
                    tanggal_pertumbuhan_field,
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
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Text("Kondisi Daun", size=20, color="black"),
                    kondisi_daun_field,
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="HAPUS", on_click=show_dialog, width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ft.OutlinedButton(text="EDIT", on_click=lambda e: page.go("/src/components/graphEditFormEntry"), width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
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

    page.bgcolor = "grey400"
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
    #     content=form_card,
    #     alignment=ft.alignment.center,
    #     padding=20,
    #     bgcolor="white"
    # )