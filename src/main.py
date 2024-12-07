import flet as ft
from components.navBar import create_navbar
from page.homePage import home_page
from page.graphPage import graph_page
from components.graphAddFormEntry import graph_add_form_entry_page
from components.graphViewPage import graph_view_page
from components.graphEditFormEntry import graph_edit_form_entry_page

def main(page: ft.Page):
    page.navigation_stack = []
    # def navigate_to(new_page):
    #     page.navigation_stack.append(page.controls.copy())
    #     page.controls.clear()
    #     new_page(page, navigate_to, go_back)
    #     page.update()

    def go_back(e):
        if page.navigation_stack:
            previous_controls = page.navigation_stack.pop()
            page.views.clear()
            page.views.extend(previous_controls)
            page.update()

    def route_change(route):
        page.navigation_stack.append(page.views.copy())
        page.views.clear()
        if page.route == "/src/page/homePage":
            page.views.append(ft.View("/page/homePage", controls=[home_page(page, go_back)]))
        elif page.route == "/informasi":
            page.views.append(ft.View("/informasi", controls=[ft.Text("Informasi Tanaman Page")]))
        elif page.route == "/src/page/graphPage":
            page.views.append(ft.View("/page/graphPage", controls=[graph_page(page, go_back)]))
        elif page.route == "/src/components/graphAddFormEntry":
            page.views.append(ft.View("/components/graphAddFormEntry", controls=[graph_add_form_entry_page(page, go_back)]))
        elif page.route == "/src/components/graphViewPage":
            page.views.append(ft.View("/components/graphViewPage", controls=[graph_view_page(page, go_back)]))
        elif page.route == "/src/components/graphEditFormEntry":
            page.views.append(ft.View("/components/graphEditFormEntry", controls=[graph_edit_form_entry_page(page, go_back)]))
        page.update()

    page.on_route_change = route_change

    page.title = "Flet app"
    page.fonts = {
        "Kantumruy-Regular": "/fonts/kantumruy-3/Kantumruy-Regular.ttf",
        "Kantumruy-Bold": "/fonts/kantumruy-3/Kantumruy-Bold.ttf",
        "Kantumruy-Light": "/fonts/kantumruy-3/Kantumruy-Light.ttf",
    }
    page.theme = ft.Theme(font_family="Kantumruy-Regular")

    page.add(create_navbar(page))

ft.app(target=main)