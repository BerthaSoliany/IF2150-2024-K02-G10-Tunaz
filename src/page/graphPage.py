import flet as ft
from datetime import date, timedelta, datetime, datetime
# import plotly.graph_objects as go
from src.components.button1 import create_button1
from src.components.navBar import create_navbar
from src.components.addButton import create_floating_action_button
from src.components.clickCard import create_click_card
from src.components.graphAddFormEntry import graph_add_form_entry_page
from src.components.graphViewPage import graph_view_page
from src.controllers.tanaman import Tanaman
from src.controllers.grafikpertumbuhan import GrafikPertumbuhan
from src.controllers.tanamancontroller import TanamanController


class State:
    toggle = True

s = State()


def graph_page(page: ft.Page):
    page.bgcolor = "white"
    page.horizontal_alignment = ft.alignment.center
    page.vertical_alignment = ft.alignment.center

    # text_refs = [ft.Ref[ft.Text]() for i in range(6)]

    def to_date(dt_date):
        yy, mm, dd = map(int, dt_date.split('-'))
        return date(yy, mm, dd)
    
    def to_date2(dt_date):
        dd, mm, yy = map(int, dt_date.split('/'))
        return date(yy, mm, dd)
    
    def dropdown_changed1(e):
        pilihan_index.options.clear()
        if(pilihan_jenis.value != None):
            index_tanaman = tanaman_controller.get_all_index_tanaman(pilihan_jenis.value)
            pilihan_index.options = [ft.dropdown.Option(option) for option in index_tanaman]
            pilihan_index.disabled = False
            pilihan_index.bgcolor = "#DBC4AB"
            pilihan_index.fill_color = "#DBC4AB"
            pilihan_index.update()
        else:
            pilihan_index.disabled = True
        pilihan_index.value = None
        pilihan_index.update()
        page.update()  

    def toggle_data(e):
        # tombol cari ini diilangin dan masukin function toggle data ke pilihan_index yaw
        page.session.set("jenis_tanaman", pilihan_jenis.value)
        page.session.set("index_tanaman", pilihan_index.value)
        tanaman_controller = TanamanController()
        icon_tanaman = tanaman_controller.get_tanaman(pilihan_jenis.value, pilihan_index.value)[3]
        page.session.set("icon_tanaman", icon_tanaman)
        
        graph = GrafikPertumbuhan()
        new_data_points, data_tanggal = graph.tinggi_terhadap_waktu(Tanaman(jenis_tanaman=pilihan_jenis.value, index_tanaman=pilihan_index.value, icon_tanaman=None, data_informasi_tanaman=None, data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None))
        if(len(new_data_points) != 0):
            range_tanggal = (to_date(data_tanggal[-1]) - to_date(data_tanggal[0])).days
            if(range_tanggal < 5):
                range_tanggal = 5
            range_tinggi = max(new_data_points)
            if(range_tinggi < 3):
                range_tinggi = 3
            # data grafik
            new_data_points = [ft.LineChartDataPoint((to_date(data_tanggal[i])-to_date(data_tanggal[0])).days, new_data_points[i]) for i in range(len(new_data_points))]
            data_1[0].data_points = new_data_points
            # scaling grafik
            chart.left_axis.labels.clear()
            chart.horizontal_grid_lines.interval=max(round(range_tinggi/7),1)
            chart.vertical_grid_lines.interval=max(round(range_tanggal/12),1)
            # chart.update()
            # for i in range(3):
            #     chart.left_axis.labels[i].value = round(range_tinggi*(i+1)/3)
            #     chart.left_axis.labels[i].label.value = round(range_tinggi*(i+1)/3)
            chart.left_axis.labels_interval = max(range_tinggi//3,1)
            range_interval = range_tinggi
            if(range_tinggi % 3 == 0):
                range_interval += 1
            chart.left_axis.labels = [
                ft.ChartAxisLabel(
                    value=i,
                    label=ft.Text(str(i), size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ) for i in range(0,int(range_interval),int(chart.left_axis.labels_interval))
            ]
            chart.left_axis.labels.append(
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Text("0", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ))
            chart.max_y = range_tinggi
            # text_refs = [ft.Ref[ft.Text]() for i in range(6)]   
            first_date = to_date(data_tanggal[0])
            # for i in range(6):
            #     chart.bottom_axis.labels[i].value = range_tanggal*i//5
                # text_refs[i].current.value = (to_date(data_tanggal[0]) + timedelta(days=range_tanggal*i//5))
            chart.max_x = range_tanggal
            # judul grafik
            chart_container.content.controls[0] = ft.Text(f"Grafik Pertumbuhan Tanaman {pilihan_jenis.value} {pilihan_index.value}", size=20, color="#5F9356", weight=ft.FontWeight.BOLD)
            # data catatan
            data_container.controls = [
                *[
                    create_click_card(page, lambda e: page.go("/src/components/graphViewPage"), f"Tinggi: {point.y}", datetime.strptime(data_tanggal[i],"%Y-%m-%d").strftime("%d/%m/%Y"))
                    for i, point in enumerate(new_data_points)
                ]
            ]
        else:
            # data grafik dummy
            new_data_points = []
            data_1[0].data_points = data1_set1
            # scaling grafik dummy
            chart.horizontal_grid_lines.interval=30//7
            chart.vertical_grid_lines.interval=30//12
            # for i in range(3):
            #     chart.left_axis.labels[i].value = 30*(i+1)/3
            #     chart.left_axis.labels[i].label.value = 30*(i+1)/3
            chart.left_axis.labels_interval = 10
            chart.left_axis.labels=[
                    ft.ChartAxisLabel(
                        value=30*(i+1)/3,
                        label=ft.Text(30*(i+1)/3, size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                    ) for i in range(3)
            ]
            chart.max_y = 30
            first_date = date.today()
            # for i in range(6):
            #     chart.bottom_axis.labels[i].value = 30*i//5
                # text_refs[i].current.value = (date.today() + timedelta(days=30*i//5))
            chart.max_x = 30
            range_tanggal = 30
            # judul grafik dummy
            chart_container.content.controls[0] = ft.Text("Tidak ada data pertumbuhan tanaman.", size=20, color="#5F9356", weight=ft.FontWeight.BOLD)
            # data catatan dummy
            data_container.controls = [ft.Text("Tidak ada data pertumbuhan tanaman.", size=16, color=ft.Colors.BLACK)]
        chart.bottom_axis.labels.clear()
        chart.bottom_axis.labels_interval = max(int(round(range_tanggal/5)),1)
        range_interval = range_tanggal
        if(range_tanggal % 5 == 0):
            range_interval += 1
        chart.bottom_axis.labels = [
                ft.ChartAxisLabel(
                    value=i,
                    label=ft.Container(
                        ft.Text(
                            (first_date + timedelta(days=i)).strftime("%d/%m/%Y"),
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ) for i in range(0,int(range_interval),int(chart.bottom_axis.labels_interval))
        ]
        chart.data_series = data_1
        chart_container.update()
        chart.update()
        data_container.update()
        fab.disabled = False
        fab.update()
        # data_container.controls = [
        #     ft.Text("Catatan Pertumbuhan", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
        #     *[
        #         ft.Text(f"Point {i+1}: x={point.x}, y={point.y}", size=14, color=ft.Colors.BLACK)
        #         for i, point in enumerate(new_data_points)
        #     ]
        # ]

    tanaman_controller = TanamanController()
    jenis_tanaman = tanaman_controller.get_all_jenis_tanaman()

    pilihan_jenis = ft.Dropdown(
            on_change=dropdown_changed1,
            text_style=ft.TextStyle(size=16, color="black", overflow=ft.TextOverflow.ELLIPSIS),
            bgcolor="#AADBA3",
            options=[ft.dropdown.Option(option) for option in jenis_tanaman],
            width=300,
            height=44,
            # max_menu_height=200,
            select_icon_enabled_color="black",
            border_width=0,
            border_radius=10,
            fill_color="#AADBA3",
            hint_content=ft.Text(value="Jenis", size=16, color="black", overflow=ft.TextOverflow.ELLIPSIS),
            content_padding=10,
            alignment=ft.Alignment(-1,0),
            disabled = False,
        )
    
    pilihan_index = ft.Dropdown(
            on_change=toggle_data,
            text_style=ft.TextStyle(size=16, color="black", overflow=ft.TextOverflow.ELLIPSIS),
            bgcolor="#E0E0E0",
            # label=judul,
            # label_style=ft.TextStyle(size=16, color="black"),
            options=[ft.dropdown.Option(option) for option in []],
            width=100,
            height=44,
            # max_menu_height=200,
            select_icon_enabled_color="black",
            # icon=ft.Icon(size=16, color="black"),
            border_width=0,
            border_radius=10,
            fill_color="#E0E0E0", #if pilihan_jenis.value else "#E0E0E0",
            hint_content=ft.Text(value="Index", size=16, color="black"),
            content_padding=5,
            alignment=ft.Alignment(0,0),
            disabled=True,
        )
    # index_tanaman = tanaman_controller.get_all_index_tanaman(pilihan_jenis.value)

    # Create an add button
    # def button_clicked(e):
    #     navigate_to(graph_add_form_entry_page)

    fab = create_floating_action_button(lambda e: page.go("/src/components/graphAddFormEntry"))
    fab.disabled = True
    # Its graph time baby
     # Create initial data sets (data dummy)
    data1_set1 = [
        ft.LineChartDataPoint(0, 15),
        ft.LineChartDataPoint(5, 15),
        ft.LineChartDataPoint(10, 15),
        ft.LineChartDataPoint(15, 15),
        ft.LineChartDataPoint(20, 15),
        ft.LineChartDataPoint(25, 15),
        ft.LineChartDataPoint(30, 15),
    ]
    data_1 = [
        ft.LineChartData(
            data_points=data1_set1,
            stroke_width=5,
            color="#5F9356",
            curved=True,
            stroke_cap_round=True,
        )
    ]
    range_tanggal = 30
    range_tinggi = 30
    tanggal_sekarang = date.today()
    # def on_card_click(e):
    #     navigate_to(graph_view_page)

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.border.all(3, ft.Colors.GREY_200),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=range_tinggi//7, color=ft.Colors.GREY_200, width=1
            # interval=1, color=ft.Colors.GREY_200, width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            # interval=1, color=ft.Colors.GREY_200, width=1
            interval=range_tanggal//12, color=ft.Colors.GREY_200, width=1
        ),
        left_axis=ft.ChartAxis(
            title=ft.Text("Tinggi Tanaman (cm)", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            labels=[
                ft.ChartAxisLabel(
                    value=range_tinggi*(i+1)/3,
                    label=ft.Text(range_tinggi*(i+1)/3, size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
                ) for i in range(3)
            ],
            labels_size=40,
            labels_interval=range_tinggi//3,
        ),
        bottom_axis=ft.ChartAxis(
            title=ft.Text("Tanggal", size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            labels=[
                ft.ChartAxisLabel(
                    value=range_tanggal*i/5,
                    label=ft.Container(
                        ft.Text(
                            (tanggal_sekarang + timedelta(days=range_tanggal*i/5)).strftime("%d/%m/%Y"),
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.BLACK,
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ) for i in range(6)
            ],
            labels_interval=range_tanggal//5,
            labels_size=32,
        ),
        tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.GREY_200),
        min_y=0,
        max_y=range_tinggi,
        min_x=0,
        max_x=range_tanggal,
        # animate=5000,
        expand=True,
        # on_chart_event=ft.ViewPopEvent.view.route()
    )
    
    title = ft.Text("Grafik Pertumbuhan Tanaman", size=20, color="#5F9356", weight=ft.FontWeight.BOLD)

    chart_container = ft.Container(
        content=ft.Column(
            controls=[
                title,
                chart,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=10,
        margin=10,
        bgcolor=ft.Colors.WHITE,
        width=850,
        height=400,
        # shadow=ft.BoxShadow(
        #     blur_radius=1,
        #     spread_radius=1,
        #     color=ft.Colors.GREY_400,
        #     offset=ft.Offset(0, 1),
        # ),
    )

    data_container = ft.ListView(
        controls=[ft.Text("Pilih jenis dan index tanaman!", size=16, color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER),],
        padding=10,
        # margin=10,
        # border=ft.border.all(3, ft.Colors.GREY_200),
        # border_radius=10,
        # bgcolor=ft.Colors.WHITE,
        divider_thickness=0,
        expand=True,
        width=300,
        height=380,
    )

    header = ft.Container(
        content=ft.Text("Catatan Pertumbuhan", size=20, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
        padding=10,
        alignment=ft.alignment.center,
        bgcolor="#5F9356",
        border_radius=ft.border_radius.only(top_left=10, top_right=10),
        width=ft.Column(expand=True),
    )
    
    bordered_container = ft.Container(
        content=ft.Column(
            controls=[
                header,
                data_container,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.END,

        ),
        # border=ft.border.all(3, ft.Colors.GREY_200),
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        padding=ft.padding.only(top=0, right=0),
        margin=10,
        shadow=ft.BoxShadow(
            blur_radius=1,
            spread_radius=1,
            color=ft.Colors.GREY_400,
            offset=ft.Offset(0, 1),
        ),
        # expand=True,
        width=300,
        # width=ft.Column(expand=True),
        alignment=ft.Alignment(1,0),
        # shadow=ft.BoxShadow
        # alignment=ft.alignment.center,
    )

    konten = ft.Stack([
    ft.Column(controls=[
        create_navbar(page),
        ft.Stack([
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        pilihan_jenis,
                        pilihan_index,
                    ],
                    alignment="start",
                    vertical_alignment="center",
                ),
                ft.Row(
                    controls=[
                        chart_container,
                        bordered_container,
                    ],
                    alignment="spaceBetween",
                    vertical_alignment="center",
                    spacing=10,
                ),
            ], right=20, bottom=20, left=20, top=5
        )
    ])
    ]),
    fab], expand=True, alignment=ft.Alignment(1,1))

    page.controls.clear()
    page.controls.append(konten)
    page.update()

    if page.session.get("jenis_tanaman") != None:
        pilihan_jenis.value = page.session.get("jenis_tanaman")
        dropdown_changed1(None)

    if page.session.get("index_tanaman") != None:
        pilihan_index.value = page.session.get("index_tanaman")
        toggle_data(None)
        
    page.update()
        
    return page