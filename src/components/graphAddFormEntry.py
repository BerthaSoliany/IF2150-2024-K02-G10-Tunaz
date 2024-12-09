import flet as ft
import datetime
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman
from src.controllers.datapertumbuhantanamancontroller import DataPertumbuhanTanamanController

def graph_add_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "white"
    page.theme = ft.Theme(font_family="Kantumruy-Regular")

    def handle_change(e):
        text_tanggal.value = "        " #
        text_tanggal.value += e.control.value.strftime('%Y-%m-%d')
        page.update()

    def handle_dismissal(e):
        # page.add(ft.Text(f"DatePicker dismissed"))
        page.add()

    # ganti placeholder textnya. kalo NONE tampilin yg masukkan, kalo ada valuenya
    text_tanggal = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="        Masukkan tanggal pertumbuhan di sini... (DD/MM/YYYY)", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    pilih_tanggal = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2023,month=1,day=1),
                          last_date=datetime.datetime.now(), 
                          on_change=handle_change,
                          on_dismiss=handle_dismissal,
                          cancel_text="Batal",
                          confirm_text="Pilih",
                          error_format_text="Format input tidak valid", 
                          field_label_text="Masukkan tanggal", 
                          help_text="Pilih tanggal")), 
        style=ft.ButtonStyle(side=ft.BorderSide(color="transparent", width=0),
                            shape=ft.RoundedRectangleBorder(radius=5), 
                            alignment=ft.Alignment(-1,0),
                            color="white"),
        width=1000,)
    tanggal_pertumbuhan_field = ft.Stack([text_tanggal,pilih_tanggal])
    tinggi_tanaman_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text="Masukkan tinggi tanaman di sini... (dalam cm)", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), keyboard_type=ft.KeyboardType.NUMBER)
    status_tanaman_dropdown = ft.Dropdown(border_radius=5, border_color="#D7D7D7",bgcolor="white", width=126, hint_content=ft.Text(value="Status", color="grey400", size="16"), border_width=1, text_style=ft.TextStyle(color="black"), options=[ft.dropdown.Option("Hidup"), ft.dropdown.Option("Mati")])
    kondisi_daun_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text="Masukkan kondisi daun di sini...", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    jenis_index = "Jagung 001" # nanti diganti sesuai tanamannya
    icon = "icon1" # nanti diganti sesuai icon tanamannya
    def on_click_add(e):
        data_pertumbuhan_controller = DataPertumbuhanTanamanController()
        data_pertumbuhan = DataPertumbuhanTanaman(status_tanaman_dropdown.value, tinggi_tanaman_field.value, text_tanggal.value[8:], kondisi_daun_field.value)
        data_pertumbuhan_controller.tambah_data_pertumbuhan("JERUK", 2, data_pertumbuhan) # nanti jeruk, 2 nya diganti sesuai tanamannya
        page.go("/src/page/graphPage")

    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(jenis_index, size=36, weight=ft.FontWeight.BOLD, color="#5F9356"),
                            ft.Image(
                            src="./img/"+ icon +".png",  
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
                        ft.OutlinedButton(text="TAMBAH", on_click=on_click_add, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
                        ft.OutlinedButton(text="BATAL", on_click=lambda e: page.go("/src/page/graphPage"), width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
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