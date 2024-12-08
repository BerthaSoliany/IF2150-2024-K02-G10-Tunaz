import flet as ft
from src.components.button1 import create_button1

def info_add_form_entry_page(page: ft.Page, go_back):
    page.horizontal_alignment = ft.alignment.center
    page.vertical_alignment = ft.alignment.center
    page.bgcolor = "white"

    # def radiogroup_changed(e):
        # t.value = f"Your favorite color is:  {e.control.value}"
        # page.update()

    # t = ft.Text()
    # cg = ft.RadioGroup(content=ft.Row([
    #     ft.Radio(value="icon1", label=ft.Image(src="/img/icon1.png", width=51, height=51, fit="contain")),
    #     ft.Radio(value="icon2", label=ft.Image(src="/img/icon2.png", width=51, height=51, fit="contain")),
    #     ft.Radio(value="icon3", label=ft.Image(src="/img/icon3.png", width=51, height=51, fit="contain")),
    #     ft.Radio(value="icon4", label=ft.Image(src="/img/icon4.png", width=51, height=51, fit="contain")),
    #     ft.Radio(value="icon5", label=ft.Image(src="/img/icon5.png", width=51, height=51, fit="contain")),
    #     ]), 
    #     on_change=radiogroup_changed)

    # def iconChoiced(e):
    #     return e.controls.value

    iconChoice = ft.Row(
        controls=[
            ft.Image(src="/img/icon1.png", width=51, height=51, fit="contain"),
            ft.Image(src="/img/icon2.png", width=51, height=51, fit="contain"),
            ft.Image(src="/img/icon3.png", width=51, height=51, fit="contain"),
            ft.Image(src="/img/icon4.png", width=51, height=51, fit="contain"),
            ft.Image(src="/img/icon5.png", width=51, height=51, fit="contain"),
        ],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )

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
                    
                    ft.Text("Jenis Tanaman", size=20, color="black"),
                    ft.CupertinoTextField(bgcolor="white", placeholder_text="Masukan jenis tanaman di sini...", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400)), 
                    ft.Text("Simbol Tanaman", size=20, color="black"),
                    iconChoice,
                    ft.Text("Kebutuhan Perawatan", size=20, color="black"),
                    ft.CupertinoTextField(bgcolor="white",placeholder_text="Masukkan kebutuhan perawatan di sini...", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), multiline=True, min_lines=5, max_lines=5),
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="TAMBAH", on_click=go_back, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
                        ft.OutlinedButton(text="BATAL", on_click=go_back, width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
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
    # ft.Container(
    #         content=form_card,
    #         alignment=ft.alignment.center,
    #         bgcolor="white",
    #     )
    # )
    # page.update()
    return ft.Container(
            content=form_card,
            alignment=ft.alignment.center,
            bgcolor="white"
    )
