import flet as ft

def main(page: ft.Page):
    page.title = "Flet app"
    
    def button_clicked(e):
        page.add(ft.Text("Button clicked!"))

    page.add(
        ft.Text("Hello, Flet!"),
    )