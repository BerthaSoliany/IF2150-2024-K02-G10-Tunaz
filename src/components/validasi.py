import flet as ft

def create_dialog(page: ft.Page, go_back):
    def handle_close_no(e):
        page.close(dialog)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_yes(e):
        page.close(dialog)
        go_back(e)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dialog = ft.AlertDialog(
        modal=True,
        content=ft.Text("Apakah Anda yakin ingin menghapus data ini?\nPenghapusan data bersifat permanen.", text_align="center", color=ft.colors.BLACK),
        actions=[
            ft.Row(
                controls=[
                    ft.OutlinedButton(text="YA", on_click=handle_close_yes, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.GREEN, shape=ft.RoundedRectangleBorder(radius=10))),
                    ft.OutlinedButton(text="TIDAK", on_click=handle_close_no, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.RED, shape=ft.RoundedRectangleBorder(radius=10))),
                ],
                alignment="center"
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(),
        bgcolor=ft.colors.YELLOW_100,
        shadow_color=ft.colors.GREY_400,
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
