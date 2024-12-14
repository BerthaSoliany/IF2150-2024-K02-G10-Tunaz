import flet as ft
from src.components.validasi import validasi
from src.controllers.tanaman import Tanaman
def info_view_page(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.theme = ft.Theme(font_family="Kantumruy-Regular")

    dialog = validasi(page, "/src/page/infoPage")
    def show_dialog(e):
        page.session.set("action", "hapus_data_informasi")
        page.open(dialog)

    def arrow_back(e):
        page.session.set("Tanaman", None)
        page.go("/src/page/infoPage")

    x = page.session.get("Tanaman")
    
    kebutuhan_perawatan_field = ft.CupertinoTextField(
        border_radius=5, 
        border=ft.border.all(1,"#D7D7D7"), 
        placeholder_text=x.get_data_informasi_tanaman().get_kebutuhan_perawatan(), 
        placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), 
        multiline=True, 
        min_lines=8, 
        max_lines=8, 
        read_only=True, 
        bgcolor="white",
        text_align=ft.TextAlign.START,
        ) # Change this
    jenis_index = x.get_jenis() + " " + str(x.get_index()) # nanti diganti sesuai tanamannya
    icon = x.get_icon() # nanti diganti sesuai icon tanamannya
    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.IconButton(icon="arrow_back", on_click=arrow_back, icon_color="#5F9356"),
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
                    ft.Text("Kebutuhan Perawatan", size=20, color="black"),
                    kebutuhan_perawatan_field,
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="HAPUS", on_click=show_dialog, width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
                        ft.OutlinedButton(text="EDIT", on_click=lambda e: page.go("/src/components/infoEditFormEntry"), width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
                        ], 
                        alignment=ft.MainAxisAlignment.END)
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
    # )