import flet as ft
from src.components.button import create_button

def main(page: ft.Page):
    page.title = "Flet app"
    
    def button_clicked(e):
        page.add(ft.Text("Button clicked!"))

    page.add(
        ft.Text("Hello, Flet!"),
        create_button("Click me", button_clicked)
    )