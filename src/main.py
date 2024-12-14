import flet as ft
from src.components.navBar import create_navbar
from src.page.graphPage import graph_page
from src.page.infoPage import info_page
from src.components.graphAddFormEntry import graph_add_form_entry_page
from src.components.graphViewPage import graph_view_page
from src.components.graphEditFormEntry import graph_edit_form_entry_page
from src.components.infoAddFormEntry import info_add_form_entry_page
from src.components.infoEditFormEntry import info_edit_form_entry_page
from src.components.infoViewPage import info_view_page
from src.components.calendarViewPage import calendar_view_page
from src.components.calendarEditFormEntry import calendar_edit_form_entry_page
from src.components.calendarAddFormEntry import calendar_add_form_entry_page
from src.components.addButton import create_floating_action_button
from src.components.clickCard import create_click_card2
from src.components.calendarRPL import calendarBody
from src.components.calendarRPL import TODAY_DATE
from src.controllers.jadwalperawatancontroller import JadwalPerawatanController
from src.controllers.jadwalperawatan import JadwalPerawatan
from src.controllers.datainformasitanamancontroller import DataInformasiTanamanController
from src.controllers.notifikasi import show_notification
import datetime
import calendar
import threading

def route_change(e: ft.RouteChangeEvent):
    page = e.page
    if page.route == "/src/main":
        main(page)
    elif page.route == "/src/page/graphPage":
        graph_page(page)
    elif page.route == "/src/page/infoPage":
        info_page(page)
    elif page.route == "/src/components/graphAddFormEntry":
        graph_add_form_entry_page(page)
    elif page.route == "/src/components/graphViewPage":
        graph_view_page(page)
    elif page.route == "/src/components/graphEditFormEntry":
        graph_edit_form_entry_page(page)
    elif page.route == "/src/components/infoEditFormEntry":
        info_edit_form_entry_page(page)
    elif page.route == "/src/components/infoAddFormEntry":
        info_add_form_entry_page(page)
    elif page.route == "/src/components/infoViewPage":
        info_view_page(page)
    elif page.route == "/src/components/calendarViewPage":
        calendar_view_page(page)
    elif page.route == "/src/components/calendarEditFormEntry":
        calendar_edit_form_entry_page(page)
    elif page.route == "/src/components/calendarAddFormEntry":
        calendar_add_form_entry_page(page)
    page.update()



def main(page: ft.Page):
    notification_thread = threading.Thread(target=show_notification, daemon=True)
    notification_thread.start()
    page.on_route_change = route_change
    page.title = "Flet app"
    page.fonts = {
        "Kantumruy-Regular": "./fonts/kantumruy-3/Kantumruy-Regular.ttf",
        "Kantumruy-Bold": "./fonts/kantumruy-3/Kantumruy-Bold.ttf",
        "Kantumruy-Light": "./fonts/kantumruy-3/Kantumruy-Light.ttf",
    }
    page.theme = ft.Theme(font_family="Kantumruy-Regular")
    page.bgcolor = "white"
    # page.padding = ft.padding.only(top=0, bottom=10, left=10, right=10)
    page.padding = ft.padding.all(0)
    
    data_container = ft.ListView(
        controls=[ft.Text("Tidak ada jadwal perawatan tanaman.", size=16, color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER)],
        padding=10,
        divider_thickness=0,
        expand=True,
        width=300,
        height=400,
        spacing=5,
    )
    page.session.set("date", TODAY_DATE)
    hari = TODAY_DATE.strftime("%A")
    bulan = calendar.month_name[TODAY_DATE.month]
    tanggal = str(TODAY_DATE.day) +' ' + bulan +' ' + str(TODAY_DATE.year)
    jadwal_perawatan_controller = JadwalPerawatanController()
    waktu_perawatan = TODAY_DATE.strftime("%Y-%m-%d")
    data1_set1 = jadwal_perawatan_controller.get_all_jadwal_perawatan_by_date(waktu_perawatan)
    if(len(data1_set1) != 0):
        data_informasi_tanaman_controller = DataInformasiTanamanController()
        for jadwal_perawatan in data1_set1:
            jadwal_perawatan[5] = jadwal_perawatan[5][11:19]
            jadwal_perawatan.append(data_informasi_tanaman_controller.get_data_informasi_tanaman(jadwal_perawatan[1], jadwal_perawatan[2])[4])
        
        data_container.controls=[
            *[
                create_click_card2(page, lambda e: page.go("/src/components/calendarViewPage"), data[5], f"{data[6]} {data[1]} {data[2]}", data[8])
                for data in data1_set1
            ]
        ]
    else:
        data_container.controls=[ft.Text("Tidak ada jadwal perawatan tanaman.", size=16, color=ft.Colors.BLACK)]

    
    header = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(hari, size=16, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                ft.Text(tanggal, size=20, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=2,
        ),
        padding=10,
        alignment=ft.Alignment(-1,0),
        bgcolor="#5F9356",
        border_radius=ft.border_radius.only(top_left=10, top_right=10),
        width=ft.Column(expand=True),
    )
    def on_date_selected(date):
        page.session.set("date", date)
        hari = date.strftime("%A")
        bulan = calendar.month_name[date.month]
        tanggal = str(date.day) +' ' + bulan +' ' + str(date.year)
        header.content.controls[0].value = hari
        header.content.controls[1].value = tanggal
        header.update()
        jadwal_perawatan_controller = JadwalPerawatanController()
        waktu_perawatan = date.strftime("%Y-%m-%d")
        data1_set1 = jadwal_perawatan_controller.get_all_jadwal_perawatan_by_date(waktu_perawatan)
        if(len(data1_set1) != 0):
            data_informasi_tanaman_controller = DataInformasiTanamanController()
            for jadwal_perawatan in data1_set1:
                jadwal_perawatan[5] = jadwal_perawatan[5][11:19]
                jadwal_perawatan.append(data_informasi_tanaman_controller.get_data_informasi_tanaman(jadwal_perawatan[1], jadwal_perawatan[2])[4])
            
            data_container.controls=[
                *[
                    create_click_card2(page, lambda e: page.go("/src/components/calendarViewPage"), data[5], f"{data[6]} {data[1]} {data[2]}", data[8])
                    for data in data1_set1
                ]
            ]
        else:
            data_container.controls=[ft.Text("Tidak ada jadwal perawatan tanaman.", size=16, color=ft.Colors.BLACK)]
        data_container.update()

    calBody = calendarBody(page, on_date_selected=on_date_selected)

    bordered_container = ft.Container(
        content=ft.Column(
            controls=[
                header,
                data_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.END,

        ),
        # border=ft.border.all(3, ft.Colors.GREY_200),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.only(top=0, right=0),
        margin=10,
        shadow=ft.BoxShadow(
            blur_radius=1,
            spread_radius=1,
            color=ft.Colors.GREY_400,
            offset=ft.Offset(0, 1),
        ),
        # expand=True,
        width=300,
        height=505,
        # width=ft.Column(expand=True),
        alignment=ft.Alignment(1,0),
        # shadow=ft.BoxShadow
        # alignment=ft.alignment.center,
    )



    def pilihan_perawatan():
        def handle_close_no(e):
            page.close(dialog)
            tipe = "Pupuk"
            page.session.set("tipe", tipe)
            page.go("/src/components/calendarAddFormEntry")
            # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

        def handle_close_yes(e):
            page.close(dialog)
            tipe = "Siram"
            page.session.set("tipe", tipe)
            page.go("/src/components/calendarAddFormEntry")
            # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

        dialog = ft.AlertDialog(
            modal=True,
            content=ft.Text("Pilih jenis perawatan yang ingin kamu jadwalkan!", text_align="center", color=ft.colors.BLACK),
            actions=[
                ft.Row(
                    controls=[
                        ft.OutlinedButton(text="Penyiraman", on_click=handle_close_yes, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#5F9356", shape=ft.RoundedRectangleBorder(radius=10))),
                        ft.OutlinedButton(text="Pemupukan", on_click=handle_close_no, width=110, style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor="#AA6E43", shape=ft.RoundedRectangleBorder(radius=10))),
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
    dialog = pilihan_perawatan()
    def show_dialog(e):
        page.open(dialog)
    fab = create_floating_action_button(show_dialog)

    konten = ft.Stack([
    ft.Column(controls=[
        create_navbar(page),
        ft.Stack([
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                      calBody,
                      bordered_container
                    ],
                    alignment="spaceBetween",
                    vertical_alignment="center",
                ),
            ], right=20, bottom=20, left=20, top=5
        )
    ])
    ]),
    fab], expand=True, alignment=ft.Alignment(1, 1))

    page.controls.clear()
    page.controls.append(konten)

    page.update()
    return page
