import flet as ft
import datetime

def calendar_add_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    def handle_change1(e):
        waktu_tanggal.value = "        " #
        waktu_tanggal.value += e.control.value.strftime('%d/%m/%Y')
        page.update()
    
    def handle_change2(e):
        sampai_tanggal.value = "        " #
        sampai_tanggal.value += e.control.value.strftime('%d/%m/%Y')
        page.update()

    def handle_change3(e):
        waktu_jam.value = "        " #
        waktu_jam.value += e.control.value.strftime('%H:%M:%S')
        page.update()

    # untuk nampilin helper text kalau input kosong
    def cek_kosong(e):
        if waktu_tanggal.value =="":
            waktu_text.value = "Kolom tidak boleh kosong"
        if waktu_jam.value == "":
            jam_text.value = "Kolom tidak boleh kosong"
        if frekuensi.value != "" and sampai_tanggal.value=="":
            tanggal_text.value = "Kolom tidak boleh kosong"
        if sampai_tanggal.value != "" and frekuensi.value =="":
            frekuensi_text.value = "Kolom tidak boleh kosong"
        page.update()
    
    # function untuk validasi input
    def check_number(e):
        if all(char.isdigit() for char in e.control.value):
            frekuensi_text.value = ""
            if len(e.control.value) == 2:
                frekuensi_text.value = "Frekuensi tidak boleh lebih dari 2 digit"
        else:
            frekuensi_text.value = "Frekuensi harus berupa angka"
        page.update()

    def on_focus(e):
        e.control.border = ft.border.all(1,"black")
        page.update()

    def on_blur(e):
        e.control.border = ft.border.all(1,"#D7D7D7")
        page.update()

    # helper text
    waktu_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    jam_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    tanggal_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    frekuensi_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    space=ft.Text("Kebutuhan perawatan hanya bisa diubah melalui halaman informasi tanaman",weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)

    waktu_tanggal = ft.CupertinoTextField(read_only=True, width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="        DD/MM/YY", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    pilih_tanggal_perawatan = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2023,month=1,day=1),
                          last_date=datetime.datetime.now(), 
                          on_change=handle_change1,
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
    waktu_tanggal_field = ft.Stack([waktu_tanggal,pilih_tanggal_perawatan])
    waktu_jam = ft.CupertinoTextField(read_only=True,width= None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="        J:M:D", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    pilih_waktu = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(ft.TimePicker(on_change=handle_change3,
                        cancel_text="Batal",
                        confirm_text="Pilih",
                        error_invalid_text="Input tidak valid", 
                        hour_label_text="Jam",
                        minute_label_text="Menit",
                        help_text="Pilih jam")), 
        style=ft.ButtonStyle(side=ft.BorderSide(color="transparent", width=0),
                            shape=ft.RoundedRectangleBorder(radius=5), 
                            alignment=ft.Alignment(-1,0),
                            color="white"),
        width=1000,)
    waktu_jam_field = ft.Stack([waktu_jam,pilih_waktu])
    frekuensi = ft.CupertinoTextField(on_blur=on_blur,on_focus=on_focus,max_length=2, on_change=check_number,width=120, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="Frekuensi jadwal", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    frekuensi1 = ft.Row(controls=[frekuensi, ft.Text("hari", size=20, color="black")], expand=True)
    sampai_tanggal = ft.CupertinoTextField(read_only=True, width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="       Masukkan tanggal akhir", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    pilih_tanggal_akhir = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2023,month=1,day=1),
                          last_date=datetime.datetime.now(), 
                          on_change=handle_change2,
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
    sampai_tanggal_field = ft.Stack([sampai_tanggal,pilih_tanggal_akhir])
    kebutuhan_perawatan_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="grey100", placeholder_text="Kebutuhan perawatan ini g bisa diubah", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), multiline=True, min_lines=3, max_lines=3, read_only=True)
    notifikasi_switch = ft.Switch(value=True,track_outline_color="#5A3E2A",active_color="#FDFFEA",active_track_color="#5A3E2A", inactive_thumb_color="#5A3E2A", inactive_track_color="#FDFFEA")
    jenis_index = "Jagung 001" # nanti diganti sesuai tanamannya
    icon = "icon1" # nanti diganti sesuai icon tanamannya
    tipe = "Penyiraman"

    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
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
                        ft.Column(expand=True, controls=[ft.Text("Waktu "+tipe, size=20, color="black"), waktu_tanggal_field, waktu_text], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                        ft.Column(expand=True,controls=[ft.Text("Jam "+tipe, size=20, color="black"), waktu_jam_field, jam_text], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                        ft.Column(expand=True,controls=[ft.Text("Sampai tanggal", size=20, color="black"), sampai_tanggal_field, tanggal_text], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                        ft.Column(expand=True,controls=[ft.Text("Frekuensi "+tipe, size=20, color="black"), frekuensi1, frekuensi_text], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                    ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.START),
                    ft.Text("Kebutuhan Perawatan", size=20, color="black"),
                    kebutuhan_perawatan_field,
                    space,
                    ft.Row(controls=[ft.Text("Notifikasi:", size=20, color="black"), notifikasi_switch], alignment=ft.MainAxisAlignment.START, vertical_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="BATAL", on_click=lambda e: page.go("/src/main"), width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ft.OutlinedButton(text="TAMBAH", on_click=lambda e: page.go("/src/main"), width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
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
    #         content=form_card,
    #         alignment=ft.alignment.center,
    #         padding=10,
    #         bgcolor="white"
    # )