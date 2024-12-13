import flet as ft
import datetime
from src.controllers.tanamancontroller import TanamanController
from src.controllers.datainformasitanamancontroller import DataInformasiTanamanController
from src.controllers.jadwalperawatan import JadwalPerawatan
from src.controllers.jadwalperawatancontroller import JadwalPerawatanController
def calendar_add_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    def tambah(e):
        if cek_kosong(e):
            return
        elif(pilihan_jenis.value == None or pilihan_index.value == None):
            return
        else:
            jadwal_perawatan_controller = JadwalPerawatanController()
            if(frekuensi.value == '' or frekuensi.value == None):
                jadwal_perawatan_controller.tambah_data_satu_jadwal_perawatan(pilihan_jenis.value, pilihan_index.value, JadwalPerawatan(group_id=0,frekuensi_perawatan=frekuensi.value, waktu_perawatan=datetime.datetime.strptime(waktu_tanggal.value[8:], "%d/%m/%Y").strftime("%Y-%m-%d") + " " + waktu_jam.value[8:], jenis_perawatan=page.session.get("tipe"), pilihan_notifikasi=notifikasi_switch.value))
            else: 
                _ = jadwal_perawatan_controller.tambah_data_group_jadwal_perawatan(pilihan_jenis.value, pilihan_index.value, JadwalPerawatan(group_id=0,frekuensi_perawatan=frekuensi.value, waktu_perawatan=datetime.datetime.strptime(waktu_tanggal.value[8:], "%d/%m/%Y").strftime("%Y-%m-%d") + " " + waktu_jam.value[8:], jenis_perawatan=page.session.get("tipe"), pilihan_notifikasi=notifikasi_switch.value), datetime.datetime.strptime(sampai_tanggal.value[8:], "%d/%m/%Y").strftime("%Y-%m-%d"))
            page.session.set("jenis_tanaman", None)
            page.session.set("index_tanaman", None)
            page.go("/src/main")

    def handle_change1(e):
        waktu_tanggal.value = "        " #
        waktu_tanggal.value += e.control.value.strftime('%d/%m/%Y')
        waktu_text.value = ""
        page.update()
    
    def handle_change2(e):
        sampai_tanggal.value = "        " #
        sampai_tanggal.value += e.control.value.strftime('%d/%m/%Y')
        tanggal_text.value = ""
        page.update()

    def handle_change3(e):
        waktu_jam.value = "        " #
        waktu_jam.value += e.control.value.strftime('%H:%M:%S')
        jam_text.value = ""
        page.update()

    # untuk nampilin helper text kalau input kosong
    def cek_kosong(e):
        res = False
        if waktu_tanggal.value =="" or waktu_tanggal.value == None or waktu_tanggal.value == "        ":
            waktu_text.value = "Kolom tidak boleh kosong"
            res = True
        else:
            waktu_text.value = ""
        if waktu_jam.value == "" or waktu_jam.value == None or waktu_jam.value == "        ":
            jam_text.value = "Kolom tidak boleh kosong"
            res = True
        else:
            jam_text.value = ""
        if (frekuensi.value != "" and frekuensi.value != None) and (sampai_tanggal.value=="" or sampai_tanggal.value == None or sampai_tanggal.value == "        "):
            tanggal_text.value = "Kolom tidak boleh kosong"
            res = True
        else:
            tanggal_text.value = ""
        if (sampai_tanggal.value != "" and sampai_tanggal.value != None and sampai_tanggal.value != "        ") and (frekuensi.value =="" or frekuensi.value == None):
            frekuensi_text.value = "Kolom tidak boleh kosong"
            res = True
        else:
            frekuensi_text.value = ""
        if (pilihan_jenis.value == "" or pilihan_jenis.value == None):
            jenis_text.value = "Kolom tidak boleh kosong"
            pilihan_jenis.border_color = "#F47A6F"
            res = True
        else:
            jenis_text.value = ""
            pilihan_jenis.border_color = "#D7D7D7"
        if(pilihan_index.value == "" or pilihan_index.value == None):
            index_text.value = "Kolom tidak boleh kosong"
            pilihan_index.border_color = "#F47A6F"
            res = True
        else:
            index_text.value = ""
            pilihan_index.border_color = "#D7D7D7"
        page.update()
        return res
        
    
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
        e.control.border_color = "black"
        page.update()

    def on_blur(e):
        e.control.border = ft.border.all(1,"#D7D7D7")
        e.control.border_color = "#D7D7D7"
        page.update()

    # helper text
    waktu_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    jam_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    tanggal_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    frekuensi_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    jenis_text = ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    index_text = ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    space=ft.Text()

    waktu_tanggal = ft.CupertinoTextField(read_only=True, width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="        DD/MM/YY", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    pilih_tanggal_perawatan = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2023,month=1,day=1),
                          last_date=datetime.datetime.now() + datetime.timedelta(days=180), 
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
    frekuensi = ft.CupertinoTextField(cursor_width=1,cursor_color="black",on_blur=on_blur,on_focus=on_focus,max_length=2, on_change=check_number,width=120, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="Frekuensi jadwal", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    frekuensi1 = ft.Row(controls=[frekuensi, ft.Text("hari", size=20, color="black")], expand=True)
    sampai_tanggal = ft.CupertinoTextField(read_only=True, width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="       Masukkan tanggal akhir", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    pilih_tanggal_akhir = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2023,month=1,day=1),
                          last_date=datetime.datetime.now() + datetime.timedelta(days=180), 
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
    kebutuhan_perawatan_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="grey100", placeholder_text="Tidak ada data kebutuhan perawatan", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), multiline=True, min_lines=3, max_lines=3, read_only=True)
    notifikasi_switch = ft.Switch(value=True,track_outline_color="#5A3E2A",active_color="#FDFFEA",active_track_color="#5A3E2A", inactive_thumb_color="#5A3E2A", inactive_track_color="#FDFFEA")
    icon = "icon1" # nanti diganti sesuai icon tanamannya
    tipe = "Penyiraman" if page.session.get("tipe") == 'Siram' else "Pemupukan"
    pilih_tanggal_perawatan.disabled = True
    pilih_waktu.disabled = True
    pilih_tanggal_akhir.disabled = True
    frekuensi.disabled = True
    notifikasi_switch.disabled = True

    tanaman_controller = TanamanController()
    jenis_tanaman = tanaman_controller.get_all_jenis_tanaman()

    def dropdown_changed1(e):
        pilihan_index.options.clear()
        if(pilihan_jenis.value != None):
            index_tanaman = tanaman_controller.get_all_index_tanaman(pilihan_jenis.value)
            pilihan_index.options = [ft.dropdown.Option(option) for option in index_tanaman]
            pilihan_index.disabled = False
        else:
            pilihan_index.disabled = True
        pilih_tanggal_perawatan.disabled = True
        pilih_waktu.disabled = True
        pilih_tanggal_akhir.disabled = True
        frekuensi.disabled = True
        notifikasi_switch.disabled = True
        pilihan_index.value = None
        pilihan_index.update()
        page.update()  

    def toggle_data(e):
        # tombol cari ini diilangin dan masukin function toggle data ke pilihan_index yaw
        page.session.set("jenis_tanaman", pilihan_jenis.value)
        page.session.set("index_tanaman", pilihan_index.value)
        data_informasi_tanaman_controller = DataInformasiTanamanController()
        kebutuhan_perawatan_field.value = data_informasi_tanaman_controller.get_data_informasi_tanaman(pilihan_jenis.value, pilihan_index.value)[4]
        tanaman_controller = TanamanController()
        icon = tanaman_controller.get_tanaman(pilihan_jenis.value, pilihan_index.value)[3]
        form_card.content.content.controls[0].controls[1].src = "./img/"+icon+".png"
        pilih_tanggal_perawatan.disabled = False
        pilih_waktu.disabled = False
        pilih_tanggal_akhir.disabled = False
        frekuensi.disabled = False
        notifikasi_switch.disabled = False
        page.update()
        
    pilihan_jenis = ft.Dropdown(
        on_change=dropdown_changed1,
        text_style=ft.TextStyle(size=16, color="black", overflow=ft.TextOverflow.ELLIPSIS),
        bgcolor="white",
        options=[ft.dropdown.Option(option) for option in jenis_tanaman],
        width=300,
        height=44,
        select_icon_enabled_color="black",
        border_width=1,
        border_radius=5,
        border_color="#D7D7D7",
        fill_color="white",
        hint_content=ft.Text(value="Jenis", size=16, color="black", overflow=ft.TextOverflow.ELLIPSIS),
        content_padding=10,
        alignment=ft.Alignment(-1,0),
        disabled = False,
        )
    
    pilihan_index = ft.Dropdown(
        on_change=toggle_data,
        on_focus=on_focus,
        on_blur=on_blur,
        text_style=ft.TextStyle(size=16, color="black", overflow=ft.TextOverflow.ELLIPSIS),
        bgcolor="white",
        options=[ft.dropdown.Option(option) for option in []],
        width=100,
        height=44,
        select_icon_enabled_color="black",
        border_width=1,
        border_radius=5,
        border_color="#D7D7D7",
        fill_color="white", #if pilihan_jenis.value else "#E0E0E0",
        hint_content=ft.Text(value="Index", size=16, color="black"),
        content_padding=5,
        alignment=ft.Alignment(0,0),
        disabled=True,
        )

    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Column(controls=[pilihan_jenis,jenis_text], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                                    ft.Column(controls=[pilihan_index,index_text], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.START),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
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
                        ft.OutlinedButton(text="TAMBAH", on_click=tambah, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
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