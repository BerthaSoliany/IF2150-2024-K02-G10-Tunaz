import flet as ft
from src.controllers.datapertumbuhantanamancontroller import DataPertumbuhanTanamanController
from src.controllers.datapertumbuhantanaman import DataPertumbuhanTanaman
from src.controllers.datainformasitanamancontroller import DataInformasiTanamanController
from src.controllers.tanamancontroller import TanamanController
from src.controllers.jadwalperawatancontroller import JadwalPerawatanController
from src.controllers.jadwalperawatan import JadwalPerawatan
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
            # page.session.set("jenis_tanaman", None)
            # page.session.set("index_tanaman", None)

        elif(page.session.get("action") == "hapus_data_informasi"):
            # data_informasi_tanaman_controller = DataInformasiTanamanController()
            # data_informasi_tanaman_controller.hapus_data_informasi_tanaman(page.session.get("Tanaman").get_jenis(), page.session.get("Tanaman").get_index())
            tanaman_controller = TanamanController()
            tanaman_controller.hapus_tanaman(page.session.get("Tanaman"))
            page.session.set("Tanaman", None)

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
        tanaman = page.session.get("Tanaman")
        jadwal_perawatan_controller = JadwalPerawatanController()
        jadwal_perawatan_controller.hapus_data_satu_jadwal_perawatan(tanaman.get_jenis(), tanaman.get_index(), tanaman.get_data_jadwal_perawatan())
        page.session.set("Tanaman", None)
        page.go(link)
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_all_event(e):
        page.close(dialog)
        tanaman = page.session.get("Tanaman")
        jadwal_perawatan_controller = JadwalPerawatanController()
        jadwal_perawatan_controller.hapus_data_group_jadwal_perawatan(tanaman.get_data_jadwal_perawatan().get_group_id())
        page.session.set("Tanaman", None)
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
        tanaman = page.session.get("Tanaman")
        tanaman_baru = page.session.get("Tanaman_baru")
        # print("ini address tanaman")
        # print(tanaman)
        # print("ini address tanamanbaruu")
        # print(tanaman_baru)
        jadwal_perawatan_controller = JadwalPerawatanController()
        group_id = jadwal_perawatan_controller.ubah_data_satu_jadwal_perawatan(tanaman.get_jenis(), tanaman.get_index(), tanaman.get_data_jadwal_perawatan(), tanaman_baru.get_data_jadwal_perawatan())
        tanaman_baru.get_data_jadwal_perawatan().set_group_id(group_id)

        page.session.set("Tanaman", tanaman_baru)
        page.session.set("Tanaman_baru", None)

        page.go("/src/components/calendarViewPage")
        # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_close_all_event(e):
        page.close(dialog)
        tanaman = page.session.get("Tanaman")
        tanaman_baru = page.session.get("Tanaman_baru")
        jadwal_perawatan_controller = JadwalPerawatanController()
        if(tanaman_baru.get_data_jadwal_perawatan().get_frekuensi_perawatan() == ''):
           group_id = jadwal_perawatan_controller.ubah_data_satu_jadwal_perawatan(tanaman.get_jenis(), tanaman.get_index(), tanaman.get_data_jadwal_perawatan(), tanaman_baru.get_data_jadwal_perawatan())
        else: 
            group_id = jadwal_perawatan_controller.ubah_data_group_jadwal_perawatan(tanaman.get_jenis(), tanaman.get_index(), tanaman_baru.get_data_jadwal_perawatan(), page.session.get("sampai_tanggal_baru"))
        tanaman_baru.get_data_jadwal_perawatan().set_group_id(group_id)
        page.session.set("Tanaman", page.session.get("Tanaman_baru"))
        page.session.set("Tanaman_baru", None)
        page.session.set("sampai_tanggal", page.session.get("sampai_tanggal_baru"))
        page.session.set("sampai_tanggal_baru", None)
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