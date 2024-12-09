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
    page.on_route_change = route_change
    page.title = "Flet app"
    page.fonts = {
        "Kantumruy-Regular": "./fonts/kantumruy-3/Kantumruy-Regular.ttf",
        "Kantumruy-Bold": "./fonts/kantumruy-3/Kantumruy-Bold.ttf",
        "Kantumruy-Light": "./fonts/kantumruy-3/Kantumruy-Light.ttf",
    }
    page.theme = ft.Theme(font_family="Kantumruy-Regular")
    page.bgcolor = "white"
    page.padding = ft.padding.only(top=0, bottom=10, left=10, right=10)

    data1_set1 = [
        ft.LineChartDataPoint(0, 3),
        ft.LineChartDataPoint(2.6, 2),
        ft.LineChartDataPoint(4.9, 5),
        ft.LineChartDataPoint(6.8, 3.1),
        ft.LineChartDataPoint(8, 4),
        ft.LineChartDataPoint(9.5, 3),
        ft.LineChartDataPoint(11, 4),
    ]
    dummy = "dummy"
    data_container = ft.ListView(
        controls=[
            *[
                create_click_card2(page, lambda e: page.go("/src/components/calendarViewPage"), f"waktu {point.y}", f"nama: {point.x}", dummy)
                for point in data1_set1
            ]
        ],
        # padding=10,
        # margin=10,
        # border=ft.border.all(3, ft.Colors.GREY_200),
        # border_radius=10,
        # bgcolor=ft.Colors.WHITE,
        divider_thickness=0,
        expand=True,
        width=300,
        height=400,
        spacing=10,
    )
    hari = "Minggu,"
    tanggal = " 1 Desember 2024"

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
    
    bordered_container = ft.Container(
        content=ft.Column(
            controls=[
                header,
                data_container,
            ],
            alignment=ft.MainAxisAlignment.START,
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
        # width=ft.Column(expand=True),
        alignment=ft.Alignment(1,0),
        # shadow=ft.BoxShadow
        # alignment=ft.alignment.center,
    )



    def pilihan_perawatan():
        def handle_close_no(e):
            page.close(dialog)
            tipe = "Penyiraman"
            page.go("/src/components/calendarAddFormEntry")
            # page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

        def handle_close_yes(e):
            page.close(dialog)
            tipe = "Pemupukan"
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

    page.controls.clear()
    page.controls.append(
        ft.Stack([
        ft.Column(
            controls=[
                create_navbar(page),
                ft.Row(
                    controls=[
                      bordered_container
                    ],
                    alignment="spaceBetween",
                    vertical_alignment="center",
                ),
            ], 
        ), fab
    ], expand=True, alignment=ft.Alignment(1,1))
    )

    page.update()
    return page
