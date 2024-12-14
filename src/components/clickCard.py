import flet as ft
from datetime import datetime, date
from src.controllers.tanaman import Tanaman
from src.controllers.datainformasitanaman import DataInformasiTanaman
from src.controllers.jadwalperawatan import JadwalPerawatan

def create_click_card(page, on_click, tinggi, tanggal):
    def handle_click(e):
        page.session.set("tinggi_tanaman", tinggi[8:])
        # page.session.set("tanggal_catatan", int(tanggal[9:]))
        page.session.set("tanggal_catatan", datetime.strptime(tanggal[9:],"%d/%m/%Y").strftime("%Y-%m-%d"))
        on_click(e)
        page.update()
    
    def handle_hover(e):
        card.content.color = ft.Colors.GREY_200
        card.content.update()

    def handle_exit(e):
        card.content.color = ft.Colors.WHITE
        card.content.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.CLICK,
        on_tap=handle_click,
        on_hover=handle_hover,
        on_exit=handle_exit,
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
        x = Tanaman(jenis_tanaman=perawatan_jenis_index.split()[1], index_tanaman=int(perawatan_jenis_index.split()[2]), icon_tanaman=None, data_informasi_tanaman=DataInformasiTanaman(kebutuhan_perawatan=kebutuhan_perawatan, waktu_tanam=None), data_pertumbuhan_tanaman=None, data_jadwal_perawatan=JadwalPerawatan(group_id=None, frekuensi_perawatan=None, waktu_perawatan=page.session.get("date").strftime("%Y-%m-%d") + " " + waktu, jenis_perawatan=perawatan_jenis_index.split()[0], pilihan_notifikasi=None))
        page.session.set("Tanaman", x)
        on_click(e)
        page.update()
    
    def handle_hover(e):
        card.content.color = ft.Colors.GREY_200
        card.content.update()

    def handle_exit(e):
        card.content.color = ft.Colors.WHITE
        card.content.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.CLICK,
        on_tap=handle_click,
        on_hover=handle_hover,
        on_exit=handle_exit,
        content=ft.Card(
            width=342,
            height=100,
            color=ft.Colors.WHITE,
            shadow_color=ft.Colors.GREY_400,
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(waktu, size=16, color="black"),
                        ft.Text(perawatan_jenis_index, size=20, color="#5F9356", weight=ft.FontWeight.BOLD, overflow=ft.TextOverflow.ELLIPSIS),
                        ft.Text(kebutuhan_perawatan, size=16, color="grey600", overflow=ft.TextOverflow.ELLIPSIS),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    spacing=1,
                ),
                padding=5,
                alignment=ft.Alignment(-1, 0),
                border_radius=10,
                border=ft.border.all(1, ft.Colors.GREY_200)
            )
        )
    )

    return card