import flet as ft
# import plotly.graph_objects as go
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

    # Its graph time baby
     # Create initial data sets
    data1_set1 = [
        ft.LineChartDataPoint(0, 3),
        ft.LineChartDataPoint(2.6, 2),
        ft.LineChartDataPoint(4.9, 5),
        ft.LineChartDataPoint(6.8, 3.1),
        ft.LineChartDataPoint(8, 4),
        ft.LineChartDataPoint(9.5, 3),
        ft.LineChartDataPoint(11, 4),
    ]
    data1_set2 = [
        ft.LineChartDataPoint(0, 3.44),
        ft.LineChartDataPoint(2.6, 3.44),
        ft.LineChartDataPoint(4.9, 3.44),
        ft.LineChartDataPoint(6.8, 3.44),
        ft.LineChartDataPoint(8, 3.44),
        ft.LineChartDataPoint(9.5, 3.44),
        ft.LineChartDataPoint(11, 3.44),
    ]

    # Create a LineChart
    data_1 = [
        ft.LineChartData(
            data_points=data1_set1,
            stroke_width=5,
            color=ft.Colors.GREEN_600,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.border.all(3, ft.Colors.GREY_200),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.Colors.GREY_200, width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.Colors.GREY_200, width=1
        ),
        left_axis=ft.ChartAxis(
            title=ft.Text("Tinggi Tanaman (cm)", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("10K", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("30K", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("50K", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ),
            ],
            labels_size=40,
        ),
        bottom_axis=ft.ChartAxis(
            title=ft.Text("Tanggal", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            labels=[
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "MAR",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Container(
                        ft.Text(
                            "JUN",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=8,
                    label=ft.Container(
                        ft.Text(
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.GREY_200),
        min_y=0,
        max_y=6,
        min_x=0,
        max_x=11,
        # animate=5000,
        expand=True,
    )


    def toggle_data(e):
        if s.toggle:
            # chart.data_series = data_2
            # chart.interactive = False
            new_data_points = data1_set2
        else:
            # chart.data_series = data_1
            # chart.interactive = True
            new_data_points = data1_set1

        data_1[0].data_points = new_data_points
        chart.update()

        data_container.content.controls = [
            ft.Text("Catatan Pertumbuhan", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            *[
                ft.Text(f"Point {i+1}: x={point.x}, y={point.y}", size=14, color=ft.Colors.BLACK)
                for i, point in enumerate(new_data_points)
            ]
        ]
        data_container.update()
        s.toggle = not s.toggle
        


    chart_container = ft.Container(
        content=chart,
        padding=10,
        margin=10,
        bgcolor=ft.Colors.WHITE,
        width=800,
        height=450,
    )

    data_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Catatan Pertumbuhan", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                *[
                    ft.Text(f"Point {i+1}: x={point.x}, y={point.y}", size=14, color=ft.Colors.BLACK)
                    for i, point in enumerate(data1_set1)
                ]
            ],
        ),
        # content=ft.Text("Catatan Pertumbuhan", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
        padding=10,
        margin=10,
        border=ft.border.all(3, ft.Colors.GREY_200),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        width=300,
        height=450,
    )
   
    page.add(
        create_navbar(page),
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        pilihan_jenis,
                        pilihan_index,
                        create_button1("Cari!", toggle_data, tcolor='black', bcolor='white'),
                    ],
                    alignment="start",
                    vertical_alignment="center",
                ),
                ft.Row(
                    controls=[
                        chart_container,
                        data_container,
                    ],
                    alignment="spaceEvenly",
                    vertical_alignment="center",
                ),
            ],
        ),
        fab,
        
        
    ) 

    page.update()