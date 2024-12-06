import flet as ft
import plotly.graph_objects as go
import os
from src.components.button1 import create_button1
from src.components.navBar import create_navbar
from src.components.addButton import create_floating_action_button


class State:
    toggle = True

s = State()

def main(page: ft.Page):
    page.bgcolor = "white"

    # Create a dropdown choice
    def dropdown_choice(judul: str, pilihan: list, bcolor: any):
        return ft.Dropdown(
            text_style=ft.TextStyle(size=16, color="black", overflow="hidden"),
            bgcolor=bcolor,
            label=judul,
            label_style=ft.TextStyle(size=16, color="black"),
            options=[ft.dropdown.Option(option) for option in pilihan],
            width=102,
            height=44,
            icon_enabled_color="black",
            border_width=0,
        )
    pilihan_jenis = dropdown_choice("Jenis", ["pisang", "jambu"], ft.colors.GREEN_300)
    pilihan_index = dropdown_choice("Index", ["1", "2"], ft.colors.BROWN_300)


    # Create an add button
    def button_clicked(e):
        page.add(ft.Text("Button clicked!"))

    fab = create_floating_action_button(button_clicked)


    # Create a graph
    # def toggle_graph(chart, data_1, data_2):
    #     if s.toggle:
    #         chart.data_series = data_2
    #         chart.interactive = False
    #     else:
    #         chart.data_series = data_1
    #         chart.interactive = True
    #     s.toggle = not s.toggle
    #     chart.update() 
    
    # # Create a graph using plotly
    # def create_line_chart(data1, data2):
    #     fig = go.Figure()
    #     fig.add_trace(go.Scatter(x=[0, 1, 2, 3], y=data1, mode='lines+markers', name='Data 1', line=dict(color='blue')))
    #     fig.add_trace(go.Scatter(x=[0, 1, 2, 3], y=data2, mode='lines+markers', name='Data 2', line=dict(color='red')))
    #     fig.update_layout(title='Line Chart', xaxis_title='X Axis', yaxis_title='Y Axis')
    #     return fig

    # # Initial data sets
    # data1_set1 = [0, 1, 2, 3]
    # data2_set1 = [3, 2, 1, 0]
    # data1_set2 = [1, 2, 3, 4]
    # data2_set2 = [4, 3, 2, 1]

    # # Create initial chart
    # chart = create_line_chart(data1_set1, data2_set1)
    
    # # Save plotly figure as an image
    # chart_image_path = "./img/line_chart.png"
    # chart.write_image(chart_image_path)
    # chart_html = chart.to_html(full_html=False)



   
    page.add(
        create_navbar(page),
        ft.Row(
            controls=[
                pilihan_jenis,
                pilihan_index,
            ],
            alignment="start",
            vertical_alignment="start",
        ),
        # ft.Image(src=chart_image_path, width=500, height=400),  # Display the chart image
        fab
    )

    # def on_close(e):
    #     if os.path.exists(chart_image_path):
    #         os.remove(chart_image_path)

    # page.on_close = on_close








# jancok cok gw pusing
import flet as ft
import plotly.graph_objects as go
import locale
from src.components.button1 import create_button1
from src.components.navBar import create_navbar
from src.components.addButton import create_floating_action_button

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


# class State:
#     toggle = True

# s = State()

in_style: dict = {
    "expand": 1,
    "bgcolor": "white",	
    "boder_radius": 10,
    "padding": 10,
}

class GraphIn(ft.Container):
    def __init__(self) -> None:
        super().__init__(**in_style)

out_style: dict = {
    "expand": 1,
    "bgcolor": "white",	
    "boder_radius": 10,
    "padding": 10,
}

class GraphOut(ft.Container):
    def __init__(self) -> None:
        super().__init__(**out_style)


tracker_style: dict = {
    "main": {
        "expand": True,
        "bgcolor": "white",
        "border_radius": 10,
    },
    "balance": {
        "size": 48,
        "weight": "bold",
    },
    "input": {
        "width": 200,
        "height": 44,
        "border_color":"black",
        "cursor_height": 16,
        "cursor_color": "black",
        "content_padding": 10,
        "text-align": "center",
    },
    "add":{
        "icon": ft.icons.ADD,
        "bgcolor": "black",
        "icon_size": 16,
        "icon_color": "teal600",
        "scale": ft.transform.Scale(0.8),
    },
    "subtract": {
        "icon": ft.icons.REMOVE,
        "bgcolor": "black",
        "icon_size": 16,
        "icon_color": "teal600",
        "scale": ft.transform.Scale(0.8),
    }
}

class Tracker(ft.Container):
    def __init__(self, _in: object, _out: object) -> None:
        super().__init__()
        self.in_ = _in
        self.out = _out

        self.counter = 0.0
        self.balance = ft.Text(
            locale.currency(self.counter, grouping=True),
            **tracker_style["balance"]
        )

        self.input = ft.TextField(**tracker_style.get("input"))
        self.add = ft.IconButton(
            **tracker_style.get("add"),
            data=True
        )
        self.subtract = ft.IconButton(
            **tracker_style.get("subtract"),
            data=False,
        )


        self.content = ft.Column(
            horizontal_alignment="center",
            controls=[
                ft.Divider(height=10, color="transparent"),
                ft.Text("Total Balance", size=11, weight="w900"),
                ft.Row(alignment="center", controls=[self.balance]),
                ft.Divider(height=10, color="transparent"),
                ft.Row(alignment="center", 
                       controls=[
                           self.subtract,
                           self.input,
                           self.add,
                           ]
                        ),
            ],
        )



def main(page: ft.Page):
    page.bgcolor = "white"

    # Create a dropdown choice
    def dropdown_choice(judul: str, pilihan: list, bcolor: any):
        return ft.Dropdown(
            text_style=ft.TextStyle(size=16, color="black", overflow="hidden"),
            bgcolor=bcolor,
            label=judul,
            label_style=ft.TextStyle(size=16, color="black"),
            options=[ft.dropdown.Option(option) for option in pilihan],
            width=102,
            height=44,
            icon_enabled_color="black",
            border_width=0,
        )
    pilihan_jenis = dropdown_choice("Jenis", ["pisang", "jambu"], ft.colors.GREEN_300)
    pilihan_index = dropdown_choice("Index", ["1", "2"], ft.colors.BROWN_300)

    # Create an add button
    def button_clicked(e):
        page.add(ft.Text("Button clicked!"))

    fab = create_floating_action_button(button_clicked)

    
    graph_in: ft.Container = GraphIn()
    graph_out: ft.Container = GraphOut()
    tracker: ft.Container = Tracker(_in=graph_in, _out=graph_out)




   
    page.add(
        create_navbar(page),
        ft.Row(
            controls=[
                pilihan_jenis,
                pilihan_index,
            ],
            alignment="start",
            vertical_alignment="start",
        ),
        fab,
        ft.Row(
            expand=True,
            controls=[
                tracker,
                ft.Column(
                    expand=True,
                    controls=[
                        graph_in,
                        graph_out,
                    ]
                )
            ]
        )
    ) 

    page.update()