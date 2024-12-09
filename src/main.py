import flet as ft
from src.components.navBar import create_navbar
from src.page.homePage import home_page
from src.page.graphPage import graph_page
from src.page.infoPage import info_page
from src.components.graphAddFormEntry import graph_add_form_entry_page
from src.components.graphViewPage import graph_view_page
from src.components.graphEditFormEntry import graph_edit_form_entry_page
from src.components.infoAddFormEntry import info_add_form_entry_page
from src.components.infoEditFormEntry import info_edit_form_entry_page
from src.components.infoViewPage import info_view_page


def route_change(e: ft.RouteChangeEvent):
    page = e.page
    if page.route == "/src/page/homePage":
        home_page(page)
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
    page.update()

def main(page: ft.Page):
    page.on_route_change = route_change
    page.title = "Flet app"
    page.fonts = {
        "Kantumruy-Regular": "/fonts/kantumruy-3/Kantumruy-Regular.ttf",
        "Kantumruy-Bold": "/fonts/kantumruy-3/Kantumruy-Bold.ttf",
        "Kantumruy-Light": "/fonts/kantumruy-3/Kantumruy-Light.ttf",
    }
    page.theme = ft.Theme(font_family="Kantumruy-Regular")
    page.bgcolor = "white"
    page.padding = ft.padding.only(top=0, bottom=10, left=10, right=10)
    page.add(create_navbar(page))
