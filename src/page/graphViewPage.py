import flet as ft
from src.page.graphEditFormEntry import graph_edit_form_entry_page
from src.components.button1 import create_button1
from src.components.validasi import create_dialog


def graph_view_page(page: ft.Page, navigate_to, go_back):
    dialog = create_dialog(page, go_back)
    def show_dialog(e):
            page.open(dialog)


    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            create_button1("Back", go_back, ft.Colors.WHITE, ft.Colors.RED),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Jagung 001", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700), # Change this to the name of the plant
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
                    ft.CupertinoTextField(placeholder_text="Masukkan tanggal", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), read_only=True), # Change this to the date of the plant
                    ft.Row(
                        [
                            ft.Column([
                                ft.Text("Tinggi Tanaman", size=20),
                                ft.CupertinoTextField(placeholder_text="Masukkan tinggi", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), read_only=True), # Change this to the height of the plant
                            ],
                            width=586,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),
                            ft.Column([
                                ft.Text("Status Tanaman", size=20),
                                ft.Dropdown(width=126, label="Hidup", options=[ft.dropdown.Option("Hidup"), ft.dropdown.Option("Mati")], disabled=True), # Change this to the status of the plant
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,),  
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Text("Kondisi Daun", size=20),
                    ft.CupertinoTextField(placeholder_text="Masukkan kondisi", placeholder_style=ft.TextStyle(color=ft.Colors.GREY_400), read_only=True), # Change this to the state of the leaves
                    ft.Row(
                        controls=[
                        ft.OutlinedButton(text="EDIT", on_click=lambda e: navigate_to(graph_edit_form_entry_page), width=142, style=ft.ButtonStyle(color=ft.Colors.GREEN_600, shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color=ft.Colors.GREEN_600, width=2))),
                        ft.OutlinedButton(text="HAPUS", on_click=show_dialog, width=142, style=ft.ButtonStyle(color=ft.Colors.RED, shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(color=ft.Colors.RED, width=2))),
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
        color=ft.Colors.YELLOW_100,
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