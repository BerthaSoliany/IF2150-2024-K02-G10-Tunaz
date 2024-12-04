import flet as ft

def create_button(text: str, on_click):
    return ft.ElevatedButton(text=text, on_click=on_click)