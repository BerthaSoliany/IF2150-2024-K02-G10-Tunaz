import flet as ft
from src.components.navBar import create_navbar
from src.components.addButton import create_floating_action_button
from src.components.infoTanamanCard import create_info_tanaman_card
from src.controllers.tanamancontroller import TanamanController
from src.controllers.datainformasitanamancontroller import DataInformasiTanamanController
from src.controllers.tanaman import Tanaman
from src.controllers.datainformasitanaman import DataInformasiTanaman
class State:
    toggle = True

s = State()

def info_page(page: ft.Page):
    page.bgcolor = "white"

    def dropdown_choice(judul: str, pilihan: list, bcolor: any): # dropdown sort by
        return ft.Dropdown(
            text_style=ft.TextStyle(size=16, color="black", overflow="hidden"),
            bgcolor=bcolor,
            hint_content=ft.Text(value=judul, size=16, color="black"),
            border_radius=12,
            # label_style=ft.TextStyle(size=16, color="black"),
            options=[ft.dropdown.Option(option) for option in pilihan],
            width=260,
            height=44,
            icon_enabled_color="black",
            border_width=0,
            content_padding=10,
        )
    
    def sorting(e):
        page.session.set("Sorting", opt_sortby.value)
        cards = []
        data_informasi_tanaman_controller = DataInformasiTanamanController()
        tanaman_controller = TanamanController()
        if(opt_sortby.value == "Jenis Tanaman (asc)"):
            data_informasi_tanaman = data_informasi_tanaman_controller.sort_by_jenis_tanaman_ascending()
        elif(opt_sortby.value == "Jenis Tanaman (desc)"):
            data_informasi_tanaman = data_informasi_tanaman_controller.sort_by_jenis_tanaman_descending()
        elif(opt_sortby.value == "Tanggal Penanaman (asc)"):
            data_informasi_tanaman = data_informasi_tanaman_controller.sort_by_waktu_tanam_ascending()
        elif(opt_sortby.value == "Tanggal Penanaman (desc)"):
            data_informasi_tanaman = data_informasi_tanaman_controller.sort_by_waktu_tanam_descending()
        else: # (opt_sortby.value == None)
            data_informasi_tanaman = data_informasi_tanaman_controller.get_all_informasi_tanaman()

        for i in range(len(data_informasi_tanaman)):  # ex ada 10 cards
            x = Tanaman(jenis_tanaman=data_informasi_tanaman[i][1], index_tanaman=data_informasi_tanaman[i][2], icon_tanaman=tanaman_controller.get_tanaman(data_informasi_tanaman[i][1],data_informasi_tanaman[i][2])[3], data_informasi_tanaman=DataInformasiTanaman(data_informasi_tanaman[i][3], data_informasi_tanaman[i][4]), data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None)
            card = create_info_tanaman_card(page, x, lambda e: page.go("/src/components/infoViewPage"))
            cards.append(card)

        # origanize cards in rows of 3
        card_rows = [ft.Row(controls=cards[i:i+3], alignment="start") for i in range(0, len(cards), 3)]
        scrollable_info_cards.content.controls = card_rows
        page.update()
    
    opt_sortby = dropdown_choice("Urutkan Berdasarkan", ["Jenis Tanaman (asc)", "Jenis Tanaman (desc)", "Tanggal Penanaman (asc)", "Tanggal Penanaman (desc)"], "#DBC4AB")
    opt_sortby.on_change = sorting
    if(page.session.get("Sorting") != None):
        opt_sortby.value = page.session.get("Sorting")
    
    def create_search_bar():
        return ft.TextField(
            label="Cari Tanaman",  
            label_style=ft.TextStyle(size=16, color="black"),
            expand=True,
            height=40,
            border_radius=16,
            border=ft.border.all(1, "#D7D7D7"),
            border_color="#D7D7D7",
            bgcolor="#FFFFFF",
            #icon="search",
            content_padding=ft.Padding(left=20, right=10, top=10, bottom=10),
            text_style=ft.TextStyle(size=16, color="black"),
        )
    
    def create_search_button():
        return ft.IconButton(
            icon=ft.icons.SEARCH,
            icon_color="black",
            # on_click=lambda e: print("Search button clicked"),
            icon_size=24,
            height=40,
            width=40,
            bgcolor="transparent", # no fill
            tooltip="Search"
        )
    
    
    fab = create_floating_action_button(lambda e: page.go("/src/components/infoAddFormEntry"))


    cards = []
    data_informasi_tanaman_controller = DataInformasiTanamanController()
    tanaman_controller = TanamanController()
    data_informasi_tanaman = data_informasi_tanaman_controller.get_all_informasi_tanaman()

    for i in range(len(data_informasi_tanaman)):  # ex ada 10 cards
        x = Tanaman(jenis_tanaman=data_informasi_tanaman[i][1], index_tanaman=data_informasi_tanaman[i][2], icon_tanaman=tanaman_controller.get_tanaman(data_informasi_tanaman[i][1],data_informasi_tanaman[i][2])[3], data_informasi_tanaman=DataInformasiTanaman(data_informasi_tanaman[i][3], data_informasi_tanaman[i][4]), data_pertumbuhan_tanaman=None, data_jadwal_perawatan=None)
        card = create_info_tanaman_card(page, x, lambda e: page.go("/src/components/infoViewPage"))
        cards.append(card)

    card_rows = [ft.Row(controls=cards[i:i+3], alignment="start") for i in range(0, len(cards), 3)]

    scrollable_info_cards = ft.Container(
            content=ft.ListView(
                controls=card_rows,
                spacing=10,
                expand=True, 
            ),
            height=470,  
            width=1440,  
            padding=10,
        )

    konten = ft.Stack([
    ft.Column(controls=[
        create_navbar(page),
        ft.Stack([
        ft.Column(controls=[
            ft.Row(
            controls=[create_search_button(), create_search_bar(), opt_sortby], 
            alignment="start", 
            vertical_alignment="center"), 
            scrollable_info_cards,
            ], right=20, bottom=20, left=20, top=5), 
        ], 
        expand=True, alignment=ft.Alignment(1,1))
    ]),
    fab], expand=True, alignment=ft.Alignment(1,1))

    page.controls.clear()
    page.controls.append(konten)
    #     create_navbar(page),
    #     ft.Column(
    #         controls=[
    #             ft.Row(
    #                 controls=[create_search_button(), create_search_bar(), opt_sortby],
    #                 alignment="start",
    #                 vertical_alignment="center",
    #             ),
    #             create_scrollable_info_cards(),  
    #         ],
    #     ), 
    #     fab,
    # )
    page.update()
    return page
