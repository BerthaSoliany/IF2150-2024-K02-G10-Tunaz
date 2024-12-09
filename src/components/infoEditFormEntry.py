import flet as ft
from src.components.button1 import create_button1

def info_edit_form_entry_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "white"
    page.theme = ft.Theme(font_family="Kantumruy-Regular")

    kebutuhan_perawatan_field = ft.CupertinoTextField(border_radius=5, border=ft.border.all(1,"#D7D7D7"), text_style=ft.TextStyle(color="black"),placeholder_text="Disiram dengan pupuk quality extra pulen yang tidak mengandung red 40. Penyiraman dilakukan dengan spray bottle atau selang dengan ukuran nozzle 0,1 mm karena daun mudah robek.", multiline=True, min_lines=10, max_lines=10,placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), bgcolor="white") # Change this
    jenis_index = "Jagung 001" # nanti diganti sesuai tanamannya
    icon = "icon1" # nanti diganti sesuai icon tanamannya
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
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="SIMPAN", on_click=lambda e: page.go("/src/components/infoViewPage"), width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
                        ft.OutlinedButton(text="BATAL", on_click=lambda e: page.go("/src/components/infoViewPage"), width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
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
    #         padding=20,
    #     )