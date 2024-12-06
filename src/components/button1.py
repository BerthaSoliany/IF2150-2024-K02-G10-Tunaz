import flet as ft

def create_button1(text: str, on_click, tcolor: str = 'primary', bcolor: str = 'secondary'):
    return ft.ElevatedButton(
        text=text, 
        on_click=on_click, 
        color=tcolor, 
        bgcolor=bcolor, 
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(8)
        ),
    )

"""
HOW TO USE

give the function to the button by making a procedure/function
def button_clicked(e):
    page.add(ft.Text("Button clicked!"))

page.add(create_button1("Click me", button_clicked, tcolor='white', bcolor='green'))
"""