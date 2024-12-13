import flet as ft
import datetime
from src.components.button1 import create_button1
from src.controllers.datapertumbuhantanamancontroller import DataPertumbuhanTanamanController
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman
def graph_edit_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    def cek_tanggal(tanggal):
        data_pertumbuhan_controller = DataPertumbuhanTanamanController()
        data_pertumbuhan = data_pertumbuhan_controller.get_all_data_pertumbuhan(page.session.get("jenis_tanaman"), page.session.get("index_tanaman"))
        for data in data_pertumbuhan:
            if data.get_tanggal_catatan() == page.session.get("data_pertumbuhan_tanaman").get_tanggal_catatan():
                return False
            if data.get_tanggal_catatan() == datetime.datetime.strptime(tanggal,"%d/%m/%Y").strftime("%Y-%m-%d"):
                return True
        return False
    
    def handle_change(e):
        tanggal_pertumbuhan.value = "        " 
        tanggal = e.control.value.strftime('%d/%m/%Y')
        if cek_tanggal(tanggal) == True:
            tanggal_text.value = "Tanggal pertumbuhan sudah ada di database. Silahkan pilih tanggal lain"
        else:
            tanggal_pertumbuhan.value += tanggal
        page.update()

    def check_number(e):
        value = e.control.value
        try:
            float(value) 
            tinggi_text.value = ""
            if len(value) == 10: 
                tinggi_text.value = "Tinggi tidak boleh lebih dari 10 digit"
        except ValueError:
            tinggi_text.value = "Tinggi tanaman harus berupa angka (misalnya, 10 atau 10.5)"
        
        page.update()

    def cek_kosong(e): 
        res = False
        if tanggal_pertumbuhan.value == "" or tanggal_pertumbuhan.value == None:
            tanggal_text.value = "Kolom tidak boleh kosong"
            res = True
        if tinggi_tanaman_field.value == "" or  tinggi_tanaman_field.value == None:
            tinggi_text.value = "Kolom tidak boleh kosong"
            res = True
        if status_tanaman_dropdown.value == "" or status_tanaman_dropdown.value == None:
            status_text.value = "Kolom tidak boleh kosong"
            res = True
        else:
            status_text.value = ""
        if tanggal_text.value != "" and tanggal_text.value != None:
            res = True
        if tinggi_text.value != "" and tinggi_text.value != None:
            res = True
        if status_text.value != "" and status_text.value != None:
            res = True
        page.update()
        return res

    def max_karakter(e):
        if len(e.control.value) == 25:
            kondisi_text.value = "Maksimal karakter yang diinput adalah 25"
        else:
            kondisi_text.value = ""
        page.update()

    def on_change(e):
        status_text.value = ""
        page.update()

    def on_focus(e):
        e.control.border = ft.border.all(1,"black")
        e.control.border_color = "black"
        page.update()

    def on_blur(e):
        e.control.border = ft.border.all(1,"#D7D7D7")
        e.control.border_color = "#D7D7D7"
        page.update()

    tanggal_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    tinggi_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    status_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    kondisi_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)

    tanggal_pertumbuhan = ft.CupertinoTextField(on_focus=on_focus, on_blur=on_blur, border_radius=5, border=ft.border.all(1,"#D7D7D7"), bgcolor="white", placeholder_text="        Masukkan tanggal", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"), read_only=True)
    tanggal_pertumbuhan.value = "        " + datetime.datetime.strptime(page.session.get("data_pertumbuhan_tanaman").get_tanggal_catatan(),"%Y-%m-%d").strftime("%d/%m/%Y")
    pilih_tanggal = ft.OutlinedButton(
        "",
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color=ft.Colors.BLACK,
        on_click=lambda e: page.open(
            ft.DatePicker(first_date=datetime.datetime(year=2023,month=1,day=1),
                          last_date=datetime.datetime.now(), 
                          on_change=handle_change,
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

    tanggal_pertumbuhan_field = ft.Stack([tanggal_pertumbuhan,pilih_tanggal])    
    tinggi_tanaman_field = ft.CupertinoTextField(on_focus=on_focus, on_blur=on_blur, max_length=10, on_change=check_number, border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text="Masukkan tinggi", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    tinggi_tanaman_field.value = page.session.get("data_pertumbuhan_tanaman").get_tinggi_tanaman()
    status_tanaman_dropdown = ft.Dropdown(on_change=on_change, on_focus=on_focus, on_blur=on_blur, icon_enabled_color="black", border_radius=5, border_color="#D7D7D7",bgcolor="white", width=126, hint_content=ft.Text(value="Hidup", color="grey400", size="16"), border_width=1, text_style=ft.TextStyle(color="black"), options=[ft.dropdown.Option("Hidup"), ft.dropdown.Option("Mati")])
    status_tanaman_dropdown.value = page.session.get("data_pertumbuhan_tanaman").get_status_tanaman()
    kondisi_daun_field = ft.CupertinoTextField(cursor_width=1,cursor_color="black", on_focus=on_focus, on_blur=on_blur, on_change=max_karakter, max_length=25, border_radius=5, border=ft.border.all(1,"#D7D7D7"),bgcolor="white", placeholder_text="Masukkan kondisi", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), text_style=ft.TextStyle(color="black"))
    kondisi_daun_field.value = page.session.get("data_pertumbuhan_tanaman").get_kondisi_daun()
    jenis_index = page.session.get("jenis_tanaman") + " " + page.session.get("index_tanaman") # nanti diganti sesuai tanamannya
    icon = page.session.get("icon_tanaman") # nanti diganti sesuai icon tanamannya

    def on_click_update(e):
        if(cek_kosong(e)):
            return
        data_pertumbuhan_controller = DataPertumbuhanTanamanController()
        data_pertumbuhan_baru = DataPertumbuhanTanaman(status_tanaman_dropdown.value, tinggi_tanaman_field.value, datetime.datetime.strptime(tanggal_pertumbuhan.value[8:],"%d/%m/%Y").strftime("%Y-%m-%d"), kondisi_daun_field.value)
        data_pertumbuhan_controller.perbarui_data_pertumbuhan(page.session.get("jenis_tanaman"), page.session.get("index_tanaman"), page.session.get("data_pertumbuhan_tanaman"),data_pertumbuhan_baru)
        page.session.set("data_pertumbuhan_tanaman", data_pertumbuhan_baru)
        page.go("/src/components/graphViewPage")
        
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
                    ft.Text("Tanggal Pertumbuhan", size=20, color="black"),
                    tanggal_pertumbuhan_field,
                    tanggal_text,
                    ft.Row(
                        [
                            ft.Column([
                                ft.Text("Tinggi Tanaman", size=20, color="black"),
                                tinggi_tanaman_field,
                                tinggi_text,
                            ],
                            width=586,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),
                            ft.Column([
                                ft.Text("Status Tanaman", size=20, color="black"),
                                status_tanaman_dropdown,
                                status_text,
                                ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),  
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Text("Kondisi Daun", size=20, color="black"),
                    kondisi_daun_field,
                    kondisi_text,
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="BATAL", on_click=lambda e: page.go("/src/components/graphViewPage"), width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ft.OutlinedButton(text="SIMPAN", on_click=on_click_update, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
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