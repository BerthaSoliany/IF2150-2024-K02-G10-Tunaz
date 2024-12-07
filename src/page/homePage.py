import flet as ft

# Home page function
def home_page(page: ft.Page, go_back):

    return ft.Column(
            controls=[
                ft.Text("Home Page", size=30),
                ft.ElevatedButton("Go to graph Page", on_click=lambda e: page.go("/src/page/graphPage")),
                ft.ElevatedButton("Back", on_click=go_back),
            ]
        )
