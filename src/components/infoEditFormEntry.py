import flet as ft
from src.components.button1 import create_button1
from src.controllers.datainformasitanamancontroller import DataInformasiTanamanController

def info_edit_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    def max_karakter(e):
        if len(e.control.value) == 200:
            kebutuhan_text.value = "Maksimal karakter yang diinput adalah 200"
        else:
            kebutuhan_text.value = ""
        page.update()
        
    x = page.session.get("Tanaman")

    def simpan(e):
        x = page.session.get("Tanaman")
        x.get_data_informasi_tanaman().set_kebutuhan_perawatan(kebutuhan_perawatan_field.value)
        page.session.set("Tanaman", x)
        data_informasi_tanaman_controller = DataInformasiTanamanController()
        data_informasi_tanaman_controller.perbarui_data_informasi_tanaman(x.get_jenis(), x.get_index(), x.get_data_informasi_tanaman())
        page.go("/src/components/infoViewPage")

    kebutuhan_text=ft.Text(weight=ft.FontWeight.NORMAL, color="#F47A6F", size=12)
    kebutuhan_perawatan_field = ft.CupertinoTextField(on_change= max_karakter, max_length=200, border_radius=5, border=ft.border.all(1,"#D7D7D7"), text_style=ft.TextStyle(color="black"), placeholder_text=x.get_data_informasi_tanaman().get_kebutuhan_perawatan(), multiline=True, min_lines=8, max_lines=8,placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), bgcolor="white") # Change this
    kebutuhan_perawatan_field.value = x.get_data_informasi_tanaman().get_kebutuhan_perawatan()
    jenis_index = x.get_jenis() + " " + str(x.get_index()) # nanti diganti sesuai tanamannya
    icon = x.get_icon() # nanti diganti sesuai icon tanamannya
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
                    ft.Text("Kebutuhan Perawatan", size=20, color="black"),
                    kebutuhan_perawatan_field,
                    kebutuhan_text,
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="BATAL", on_click=lambda e: page.go("/src/components/infoViewPage"), width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ft.OutlinedButton(text="SIMPAN", on_click=simpan, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
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
    #     )