import flet as ft
import datetime
from src.components.validasi import validasi_edit_jadwal
from src.controllers.tanaman import Tanaman
from src.controllers.tanamancontroller import TanamanController
from src.controllers.jadwalperawatancontroller import JadwalPerawatanController
from src.controllers.jadwalperawatan import JadwalPerawatan

def calendar_edit_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    dialog = validasi_edit_jadwal(page)
    def show_dialog(e):
        if (cek_kosong(e)):
            return
        # if frekuensi.value != None and sampai_tanggal.value==None:
        #     pass
        # if sampai_tanggal.value != None and frekuensi.value ==None:
        #     pass
        else:
            x = page.session.get("Tanaman")
            tanaman_baru = Tanaman(jenis_tanaman=x.get_jenis(), index_tanaman=x.get_index(), icon_tanaman=x.get_icon(), data_informasi_tanaman=x.get_data_informasi_tanaman(), data_pertumbuhan_tanaman=x.get_data_pertumbuhan_tanaman(), data_jadwal_perawatan=x.get_data_jadwal_perawatan())
            # print(waktu_tanggal.value[8:].replace("/", "-") + " " + waktu_jam.value[8:])
            tanaman_baru.set_data_jadwal_perawatan(JadwalPerawatan(group_id = tanaman_baru.get_data_jadwal_perawatan().get_group_id(), frekuensi_perawatan=frekuensi.value, waktu_perawatan= datetime.datetime.strptime(waktu_tanggal.value[8:], "%d/%m/%Y").strftime("%Y-%m-%d") + " " + waktu_jam.value[8:], jenis_perawatan=tanaman_baru.get_data_jadwal_perawatan().get_jenis_perawatan(), pilihan_notifikasi=notifikasi_switch.value))
            if frekuensi.value == None:
                page.session.set("sampai_tanggal_baru", None)
            else:
                page.session.set("sampai_tanggal_baru",datetime.datetime.strptime(sampai_tanggal.value[8:], "%d/%m/%Y").strftime("%Y-%m-%d"))
            page.session.set("Tanaman_baru", tanaman_baru)
            page.open(dialog)

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
        page.update()
        return res

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

    waktu_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    jam_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    tanggal_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    frekuensi_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    space=ft.Text()

    waktu_tanggal = ft.CupertinoTextField(read_only=True, width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="        01/12/2024", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_600), text_style=ft.TextStyle(color="black"))
    pilih_tanggal_perawatan = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2020,month=1,day=1),
                          last_date=datetime.datetime.now() + datetime.timedelta(days=1095), 
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
    waktu_jam = ft.CupertinoTextField(read_only=True,width= None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="        10 : 00 : 00", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_600), text_style=ft.TextStyle(color="black"))
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
    frekuensi = ft.CupertinoTextField(cursor_width=1,cursor_color="black",on_blur=on_blur, on_focus=on_focus,max_length=2, on_change=check_number,width=120, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="2", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_600), text_style=ft.TextStyle(color="black"))
    frekuensi1 = ft.Row(controls=[frekuensi, ft.Text("hari", size=20, color="black")], expand=True)
    sampai_tanggal = ft.CupertinoTextField(read_only=True, width=None, content_padding=5, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="       01/11/2025", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_600), text_style=ft.TextStyle(color="black"))
    pilih_tanggal_akhir = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2020,month=1,day=1),
                          last_date=datetime.datetime.now() + datetime.timedelta(days=1095), 
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
    tanaman = page.session.get("Tanaman")
    jadwal_perawatan_controller = JadwalPerawatanController()
    jadwal_perawatan = jadwal_perawatan_controller.get_one_jadwal_perawatan(tanaman.get_jenis(), tanaman.get_index(), tanaman.get_data_jadwal_perawatan())
    last_date = jadwal_perawatan_controller.get_sampai_tanggal_by_group_id(jadwal_perawatan[3])
    waktu_tanggal.value = "        " #
    waktu_tanggal.value += datetime.datetime.strptime(jadwal_perawatan[5].split()[0], "%Y-%m-%d").strftime("%d/%m/%Y")
    frekuensi.value = jadwal_perawatan[4]
    sampai_tanggal.value = "        " #
    if(frekuensi.value != None):
        sampai_tanggal.value += datetime.datetime.strptime(last_date,"%Y-%m-%d").strftime("%d/%m/%Y")

    waktu_jam.value = "        " #
    waktu_jam.value += jadwal_perawatan[5].split()[1]
    kebutuhan_perawatan_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="grey100", placeholder_text=tanaman.get_data_informasi_tanaman().get_kebutuhan_perawatan(), placeholder_style=ft.TextStyle(color=ft.Colors.GREY_600), text_style=ft.TextStyle(color="black"), multiline=True, min_lines=3, max_lines=3, read_only=True) #ini emg g bisa diubah
    notifikasi_switch = ft.Switch(value=True if jadwal_perawatan[7]==1 else False,track_outline_color="#5A3E2A",active_color="#FDFFEA",active_track_color="#5A3E2A", inactive_thumb_color="#5A3E2A", inactive_track_color="#FDFFEA")
    jenis_index = tanaman.get_jenis() + " " + str(tanaman.get_index()) # nanti diganti sesuai tanamannya
    tanaman_controller = TanamanController()
    icon = tanaman_controller.get_tanaman(tanaman.get_jenis(), tanaman.get_index())[3] # nanti diganti sesuai icon tanamannya
    tipe = "Penyiraman" if jadwal_perawatan[6] == "Siram" else "Pemupukan" # nanti diganti sesuai jenis perawatannya

    
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
                        ft.OutlinedButton(text="BATAL", on_click=lambda e: page.go("/src/components/calendarViewPage"), width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ft.OutlinedButton(text="SIMPAN", on_click=show_dialog, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
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
    #         padding=20,
    #         bgcolor="white"
    #     )