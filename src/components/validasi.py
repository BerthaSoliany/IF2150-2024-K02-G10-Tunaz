import flet as ft

def create_dialog(page: ft.Page):
    def handle_close(e):
        page.close(dialog)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dialog = ft.AlertDialog(
        modal=True,
        content=ft.Text("Apakah Anda yakin ingin menghapus data ini?\nPenghapusan data bersifat permanen.", text_align="center", color=ft.colors.BROWN_700, weight="bold"),
        actions=[
            ft.Row(
                controls=[
                    ft.TextButton("YA", on_click=handle_close, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.GREEN)),
                    ft.TextButton("TIDAK", on_click=handle_close, style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=ft.colors.RED)),
                ],
                alignment="center"
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(),
        bgcolor=ft.colors.YELLOW_100,
    )
    return dialog
"""
HOW TO USE

define the dialog by creating a variable and make a procedure/function to handle the dialog when a button is clicked
dialog = create_dialog(page)
def show_dialog(e):
        page.open(dialog)

page.add(create_button1("tambah", on_click=show_dialog))
"""
