import flet as ft

def create_floating_action_button(on_click):
    return ft.FloatingActionButton(
        content=ft.Text("+", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        # icon=ft.icons.ADD,
        on_click=on_click,
        bgcolor="#5A3E2A",
        shape=ft.RoundedRectangleBorder(10),
        tooltip="Add",
        bottom=10,
        right=10,
    )

"""
HOW TO USE

give a funtion to the button by making a procedure/function
def button_clicked(e):
    page.add(ft.Text("Button clicked!"))

fab = create_floating_action_button(button_clicked)
page.add(fab)
"""