import flet as ft
from components.button1 import create_button1


def graph_add_form_entry_page(page: ft.Page, go_back):
    page.horizontal_alignment = ft.alignment.center
    page.vertical_alignment = ft.alignment.center
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
                            ft.Text("Jagung 001", size=36, weight=ft.FontWeight.BOLD, color="#5F9356"),
                            ft.Image(
                            src="./img/icon1.png",  
                            width=55, 
                            height=55,  
                            fit="contain" 
                            ),
                        ],
                        alignment=ft.CrossAxisAlignment.STRETCH,
                    ),
                    ft.Text("Tanggal Pertumbuhan", size=20),
                    ft.CupertinoTextField(placeholder_text="Masukkan tanggal pertumbuhan di sini... (DD/MM/YYYY)", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400)), 
                    ft.Row(
                        [
                            ft.Column([
                                ft.Text("Tinggi Tanaman", size=20),
                                ft.CupertinoTextField(placeholder_text="Masukkan tinggi tanaman di sini... (dalam cm)", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400)), 
                            ],
                            width=586,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),
                            ft.Column([
                                ft.Text("Status Tanaman", size=20),
                                ft.Dropdown(width=126, hint_text="Status", options=[ft.dropdown.Option("Hidup"), ft.dropdown.Option("Mati")]), 
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),  
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Text("Kondisi Daun", size=20),
                    ft.CupertinoTextField(placeholder_text="Masukkan kondisi daun di sini...", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400)),
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="SIMPAN", on_click=go_back, width=142, style=ft.ButtonStyle(color="#5F9356", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#5F9356", width=2))),
                        ft.OutlinedButton(text="HAPUS", on_click=go_back, width=142, style=ft.ButtonStyle(color="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color="#F47A6F", width=2))),
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
    #         padding=20,
    #     )
    # )
    # page.update()
    return ft.Container(
            content=form_card,
            alignment=ft.alignment.center,
            padding=10
    )