import flet as ft
from datetime import date
from src.controllers.tanaman import Tanaman
from src.controllers.tanamancontroller import TanamanController 
from src.controllers.datainformasitanaman import DataInformasiTanaman
from src.controllers.datainformasitanamancontroller import DataInformasiTanamanController

def info_add_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    icon_option = [
        {"value": "icon1", "image": "./img/icon1.png"},
        {"value": "icon2", "image": "./img/icon2.png"},
        {"value": "icon3", "image": "./img/icon3.png"},
        {"value": "icon4", "image": "./img/icon4.png"},
        {"value": "icon5", "image": "./img/icon5.png"},
    ]

    selected_icon = ft.Ref[str]()
    selected_icon.current = "icon1"

    icon_row_ref = ft.Ref[ft.Row]()

    def on_option_select(e):
        selected_icon.current = e.control.data

        icon_row_ref.current.controls = build_options()
        page.update()

    def build_options():
        return [
            ft.Container(
                content=ft.Image(
                    src=option["image"], width=40, height=40, fit=ft.ImageFit.CONTAIN
                ),
                padding=5,
                border=ft.border.all(
                    1,
                    ft.Colors.BROWN_100 if selected_icon.current == option["value"] else ft.Colors.TRANSPARENT
                ),
                on_click=on_option_select,
                data=option["value"],
                border_radius=50,
                bgcolor=ft.Colors.BROWN_100 if selected_icon.current == option["value"] else ft.Colors.TRANSPARENT,
            
            )
            for option in icon_option
        ]

    def tambah(e):
        if jenis_tanaman_field.value:
            tanaman_controller = TanamanController()
            tanaman = Tanaman(jenis_tanaman=jenis_tanaman_field.value, index_tanaman=0, icon_tanaman=selected_icon.current, data_informasi_tanaman=None, data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None)
            tanaman.set_index(tanaman_controller.tambah_tanaman(tanaman))
            tanaman.set_data_informasi_tanaman(DataInformasiTanaman(kebutuhan_perawatan=kebutuhan_perawatan_field.value, waktu_tanam=date.today()))
            data_informasi_tanaman_controller = DataInformasiTanamanController()
            data_informasi_tanaman_controller.tambah_data_informasi_tanaman(tanaman.get_jenis(), tanaman.get_index(), tanaman.get_data_informasi_tanaman())
            page.go("/src/page/infoPage")

    def build_ui():
        return ft.Column(
            controls=[
                ft.Text("Jenis Tanaman", size=20, color="black"),
                jenis_tanaman_field,
                jenis_text,
                ft.Text("Simbol Tanaman", size=20, color="black"),
                ft.Row(ref=icon_row_ref, controls=build_options()),  # Use ref for dynamic updates
                ft.Text("Kebutuhan Perawatan", size=20, color="black"),
                kebutuhan_perawatan_field,
                kebutuhan_text,
                ft.Row(
                    controls=[
                        ft.OutlinedButton(
                            text="BATAL",
                            on_click=lambda e: page.go("/src/page/infoPage"),
                            width=142,
                            style=ft.ButtonStyle(
                                color="#F47A6F",
                                shape=ft.RoundedRectangleBorder(radius=10),
                                side=ft.BorderSide(color="#F47A6F", width=2),
                            ),
                        ),
                        ft.OutlinedButton(
                            text="TAMBAH",
                            on_click=tambah,
                            width=142,
                            style=ft.ButtonStyle(
                                color="#5F9356",
                                shape=ft.RoundedRectangleBorder(radius=10),
                                side=ft.BorderSide(color="#5F9356", width=2),
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

    def cek_kosong(e):
        if jenis_tanaman_field.value == "":
            jenis_text.value = "Jenis Tanaman tidak boleh kosong"
        page.update()

    def max_karakter_kebutuhan(e):
        if len(e.control.value) == 200:
            kebutuhan_text.value = "Maksimal karakter yang diinput adalah 200"
        else:
            kebutuhan_text.value = ""
        page.update()

    def max_karakter_jenis(e):
        if len(e.control.value) == 25:
            jenis_text.value = "Maksimal karakter yang diinput adalah 25"
        else:
            jenis_text.value = ""
        page.update()
    
    def on_focus(e):
        e.control.border = ft.border.all(1,"black")
        page.update()

    def on_blur(e):
        e.control.border = ft.border.all(1,"#D7D7D7")
        page.update()

    kebutuhan_text = ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    jenis_text = ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)

    jenis_tanaman_field = ft.CupertinoTextField(
        cursor_width=1,
        cursor_color="black",
        on_focus=on_focus,
        on_blur=on_blur,
        on_change=max_karakter_jenis,
        max_length=25,
        border_radius=5,
        border=ft.border.all(1, "#D7D7D7"),
        bgcolor="white",
        text_style=ft.TextStyle(color="black"),
        placeholder_text="Masukan jenis tanaman di sini...",
        placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400),
    )

    kebutuhan_perawatan_field = ft.CupertinoTextField(
        cursor_width=1,
        cursor_color="black",
        on_focus=on_focus,
        on_blur=on_blur,
        on_change=max_karakter_kebutuhan,
        max_length=200,
        border_radius=5,
        border=ft.border.all(1, "#D7D7D7"),
        bgcolor="white",
        text_style=ft.TextStyle(color="black"),
        placeholder_text="Masukkan kebutuhan perawatan di sini...",
        placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400),
        multiline=True,
        min_lines=3,
        max_lines=3,
        text_align=ft.TextAlign.START,
    )

    form_card = ft.Card(
        content=ft.Container(
            content=build_ui(),
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
        )
    )
    page.update()
