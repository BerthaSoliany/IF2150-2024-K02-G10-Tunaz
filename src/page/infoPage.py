import flet as ft
from src.components.navBar import create_navbar
from src.components.addButton import create_floating_action_button
from src.components.infoTanamanCard import create_info_tanaman_card

class State:
    toggle = True

s = State()

def info_page(page: ft.Page):
    page.bgcolor = "white"

    def dropdown_choice(judul: str, pilihan: list, bcolor: any): # dropdown sort by
        return ft.Dropdown(
            text_style=ft.TextStyle(size=16, color="black", overflow="hidden", font_family="Verdana"),
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
    
    opt_sortby = dropdown_choice("Urutkan Berdasarkan", ["Jenis Tanaman (asc)", "Jenis Tanaman (desc)", "Tanggal Penanaman (asc)", "Tanggal Penanaman (desc)"], "#DBC4AB")
    
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

    def create_scrollable_info_cards():
        cards = []
        for i in range(10):  # ex ada 10 cards
            card = create_info_tanaman_card(page, lambda e: page.go("/src/components/infoViewPage"))
            cards.append(card)

        # origanize cards in rows of 3
        card_rows = [ft.Row(controls=cards[i:i+3], alignment="start") for i in range(0, len(cards), 3)]

        return ft.Container(
            content=ft.ListView(
                controls=card_rows,
                spacing=10,
                expand=True, 
            ),
            height=480,  
            width=1440,  
            padding=10,
        )

    
    page.controls.clear()
    page.controls.append(ft.Stack([
        ft.Column(controls=[
            create_navbar(page),
            ft.Row(
            controls=[create_search_button(), create_search_bar(), opt_sortby], 
            alignment="start", 
            vertical_alignment="center"), 
            create_scrollable_info_cards()
            ]), 
        fab
        ], 
        expand=True, alignment=ft.Alignment(1,1)))
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
