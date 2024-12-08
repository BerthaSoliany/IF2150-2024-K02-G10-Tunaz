import flet as ft
from src.components.button1 import create_button1
from src.components.validasi import create_dialog

def info_view_page(page: ft.Page, go_back):
    page.horizontal_alignment = ft.alignment.center
    page.vertical_alignment = ft.alignment.center
    page.bgcolor = "white"
    page.theme = ft.Theme(font_family="Kantumruy-Regular")

    dialog = create_dialog(page, go_back)
    def show_dialog(e):
            page.open(dialog)

    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            create_button1("Back", go_back, ft.Colors.WHITE, "#F47A6F"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Jagung 001", size=36, weight=ft.FontWeight.BOLD, color="#5F9356"), # Change this to the name of the plant
                            ft.Image(
                            src="./img/icon1.png",  
                            width=55, 
                            height=55,  
                            fit="contain" 
                            ),
                        ],
                        alignment="spaceBetween",
                    ),
                    ft.Text("Kebutuhan Perawatan", size=20, color="black"),
                    ft.CupertinoTextField(placeholder_text="Disiram dengan pupuk quality extra pulen yang tidak mengandung red 40. Penyiraman dilakukan dengan spray bottle atau selang dengan ukuran nozzle 0,1 mm karena daun mudah robek.", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), multiline=True, min_lines=10, max_lines=10, read_only=True, bgcolor="white"), # Change this
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="EDIT", on_click=lambda e: page.go("/src/components/infoEditFormEntry"), width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
                        ft.OutlinedButton(text="HAPUS", on_click=show_dialog, width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
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

    # page.controls.clear()
    # page.controls.append(
    #     ft.Container(
    #         content=form_card,
    #         alignment=ft.alignment.center,
    #         padding=20,
    #     )
    # )
    # page.update()
    return ft.Container(
        content=form_card,
        alignment=ft.alignment.center,
        padding=20,
    )