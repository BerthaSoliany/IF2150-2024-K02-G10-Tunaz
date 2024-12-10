import flet as ft
from src.controllers.datapertumbuhantanamancontroller import DataPertumbuhanTanamanController
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman
def validasi(page: ft.Page, link):
    def handle_close_no(e):
        page.session.set("action", None)
        page.close(dialog)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_yes(e):
        if(page.session.get("action") == "hapus_data_pertumbuhan"):
            data_pertumbuhan_tanaman_controller = DataPertumbuhanTanamanController()
            data_pertumbuhan_tanaman_controller.hapus_data_pertumbuhan(page.session.get("jenis_tanaman"), page.session.get("index_tanaman"), page.session.get("data_pertumbuhan_tanaman"))  
            page.session.set("data_pertumbuhan_tanaman", None)
            page.session.set("jenis_tanaman", None)
            page.session.set("index_tanaman", None)

        page.session.set("action", None)
        page.close(dialog)
        page.go(link)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dialog = ft.AlertDialog(
        modal=True,
        content=ft.Text("Apakah Anda yakin ingin menghapus data ini?\nPenghapusan data bersifat permanen.", text_align="center", color=ft.colors.BLACK),
        actions=[
            ft.Row(
                controls=[
                    ft.OutlinedButton(text="YA", on_click=handle_close_yes, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#42AD55", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=0))),
                    ft.OutlinedButton(text="TIDAK", on_click=handle_close_no, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=0))),
                ],
                alignment="center"
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(),
        bgcolor="#FDFFEA",
        shadow_color=ft.colors.GREY_400,
    )
    return dialog


def validasi_hapus_jadwal(page: ft.Page, link):
    def handle_close_no(e):
        page.close(dialog)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_only(e):
        page.close(dialog)
        page.go(link)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_all_event(e):
        page.close(dialog)
        page.go(link)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dialog = ft.AlertDialog(
        modal=True,
        content=ft.Text("Apakah Anda yakin ingin menghapus data ini?\nPenghapusan data bersifat permanen.", text_align="center", color=ft.colors.BLACK),
        actions=[
            ft.Row(
                controls=[
                    ft.OutlinedButton(text="Event ini saja", on_click=handle_close_only, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#42AD55", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=0))),
                    ft.OutlinedButton(text="Semua event", on_click=handle_close_all_event, width=110, style=ft.ButtonStyle(color="#42AD55", bgcolor="white", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=1,color="#42AD55"))),
                    ft.OutlinedButton(text="Tidak", on_click=handle_close_no, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=0))),
                ],
                alignment="center"
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(),
        bgcolor="#FDFFEA",
        shadow_color=ft.colors.GREY_400,
    )
    return dialog

def validasi_edit_jadwal(page: ft.Page):
    def handle_close_no(e):
        page.close(dialog)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_only(e):
        page.close(dialog)
        page.go("/src/components/calendarViewPage")
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_all_event(e):
        page.close(dialog)
        page.go("/src/main")
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dialog = ft.AlertDialog(
        modal=True,
        content=ft.Text("Apakah Anda yakin ingin mengubah jadwal ini?", text_align="center", color=ft.colors.BLACK),
        actions=[
            ft.Row(
                controls=[
                    ft.OutlinedButton(text="Event ini saja", on_click=handle_close_only, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#42AD55", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=0))),
                    ft.OutlinedButton(text="Semua event", on_click=handle_close_all_event, width=110, style=ft.ButtonStyle(color="#42AD55", bgcolor="white", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=1,color="#42AD55"))),
                    ft.OutlinedButton(text="Tidak", on_click=handle_close_no, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#F47A6F", shape=ft.RoundedRectangleBorder(radius=10), side=ft.BorderSide(width=0))),
                ],
                alignment="center"
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(),
        bgcolor="#FDFFEA",
        shadow_color=ft.colors.GREY_400,
    )
    return dialog