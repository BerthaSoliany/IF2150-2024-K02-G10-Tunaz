import flet as ft

def create_floating_action_button(on_click):
    return ft.FloatingActionButton(
        icon=ft.icons.ADD,
        on_click=on_click,
        bgcolor=ft.colors.BROWN_700,
        shape=ft.RoundedRectangleBorder(10),
        tooltip="Add"
    )

"""
HOW TO USE

give a funtion to the button by making a procedure/function
def button_clicked(e):
    page.add(ft.Text("Button clicked!"))

fab = create_floating_action_button(button_clicked)
page.add(fab)
"""