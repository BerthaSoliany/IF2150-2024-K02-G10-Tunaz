import flet as ft
from src.components.button1 import create_button1
from src.components.validasi import validasi_hapus_jadwal


def calendar_view_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(font_family="Kantumruy-Regular")

    dialog = validasi_hapus_jadwal(page, "/src/main")
    def show_dialog(e):
        page.open(dialog)
    
    waktu_tanggal = ft.CupertinoTextField(width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="01/12/2024", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    waktu_jam = ft.CupertinoTextField(width= None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="10 : 00 : 00", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    frekuensi = ft.CupertinoTextField(width=120, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="2", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    frekuensi1 = ft.Row(controls=[frekuensi, ft.Text("hari", size=20, color="black")], expand=True)
    sampai_tanggal = ft.CupertinoTextField(width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="01/11/2025", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    kebutuhan_perawatan_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text="Masukkan kondisi", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True, multiline=True, min_lines=3, max_lines=3)
    notifikasi_switch = ft.Switch(value=True,track_outline_color="#5A3E2A",disabled=True, thumb_color="#FDFFEA",track_color="#5A3E2A") #seusain kalo valuenya false, itu color di switch (khusus untuk page ini doang)
    jenis_index = "Jagung 001" # nanti diganti sesuai tanamannya
    icon = "icon1" # nanti diganti sesuai icon tanamannya
    tipe = "Penyiraman"
    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(icon="arrow_back", on_click=lambda e: page.go("/src/main"), icon_color="#5F9356"),
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
                    ft.Row(controls=[
                        ft.Column(expand=True, controls=[ft.Text("Waktu "+tipe, size=20, color="black"), waktu_tanggal], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                        ft.Column(expand=True,controls=[ft.Text("Jam "+tipe, size=20, color="black"), waktu_jam], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                        ft.Column(expand=True,controls=[ft.Text("Sampai tanggal", size=20, color="black"), sampai_tanggal], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                        ft.Column(expand=True,controls=[ft.Text("Frekuensi "+tipe, size=20, color="black"), frekuensi1], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                    ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                    ft.Text("Kebutuhan Perawatan", size=20, color="black"),
                    kebutuhan_perawatan_field,
                    ft.Row(controls=[ft.Text("Notifikasi:", size=20, color="black"), notifikasi_switch], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="HAPUS", on_click=show_dialog, width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ft.OutlinedButton(text="EDIT", on_click=lambda e: page.go("/src/components/calendarEditFormEntry"), width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
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