import flet as ft
from flet import *
from flet import UserControl
import calendar
import datetime
from src.controllers.jadwalperawatancontroller import JadwalPerawatanController

CELL_SIZE = (28,28)
CELL_BG_COLOR = "green200"
TODAY_BG_COLOR = "teal600"
HORIZONTAL_LENGTH = 750

TODAY_DATE = datetime.date.today()

class SetCalendar(UserControl): 
    def __init__(self, start_year=datetime.date.today().year, page=None, on_date_selected=None):
        self.notes = {} #dict
        self.current_year = start_year
        
        self.m1=datetime.date.today().month
        self.m2=self.m1+1

        self.click_count: list = []
        
        self.current_color = "blue"

        self.selected_date = any

        self.calendar_grid = Column(
             wrap=True,
             alignment=MainAxisAlignment.CENTER,
             horizontal_alignment=CrossAxisAlignment.CENTER,
        )

        self.previous_selected_container = None #track prev

        self.page = page

        self.on_date_selected = on_date_selected
        super().__init__()





    def _change_month(self, delta):
        self.page.session.clear()
        self.previous_selected_container = None
        if(delta > 0):
            if(self.m1 ==12):
                self.current_year +=1
                self.m1 = 1
                self.m2 = 2
            else:
                self.m1 = self.m1 + 1
                self.m2 = self.m2 + 1
        else:
            if(self.m1 == 1):
                self.current_year-=1
                self.m1 = 12
                self.m2 = 13
            elif(self.m2 == 1):
                self.m1 -=1
                self.m2 = 12
            else:
                self.m1 = self.m1 - 1
                self.m2 = self.m2 - 1
        new_calendar = self.create_month_calendar(self.current_year)
        self.calendar_grid = new_calendar
        self.update()





    def one_click_date(self, e):
        if self.previous_selected_container:
            if(self.page.session.get(str(self.page.session.get("prev_selected"))) == 1):
                self.previous_selected_container.bgcolor = "#AFC9AB"
            else:
                self.previous_selected_container.bgcolor = "white"
            # if self.selected_date == datetime.date.today():
            #     self.previous_selected_container.border = border.all(2, "black")
            
            self.previous_selected_container.update()

        self.selected_date = e.control.data
        globals()["TODAY_DATE"] = self.selected_date
        # print(TODAY_DATE)

        if(self.on_date_selected):
            self.on_date_selected(self.selected_date)

        e.control.content.bgcolor = "#5F9356"
        e.control.content.update()
        # self.previous_selected_container_2 = self.previous_selected_container
        self.page.session.set("prev_selected", self.selected_date.day)
        self.previous_selected_container = e.control.content
        # self.update_notes_display()
        pass


    def create_circle(self, datee, colorr):
        datee = str(datee)
        return Container(
            content=Text(datee, size=20, color="#5A3E2A", weight=FontWeight.BOLD),
            width=45,  # Diameter of the circle
            height=45,
            bgcolor=colorr,  # Background color of the circle
            border_radius=25,  # Half of the width/height
            alignment=alignment.center,
            
        )
    
    def create_circle2(self, datee, colorr):
        datee = str(datee)
        return Container(
            content=Text(datee, size=20, color="black", weight=FontWeight.BOLD),
            width=45,  # Diameter of the circle
            height=45,
            bgcolor=colorr,  # Background color of the circle
            border_radius=25,  # Half of the width/height
            alignment=alignment.center,
            border=border.all(2, "black"),
            
        )
    
    def create_month_calendar(self, year):
        self.current_year = year
        self.calendar_grid.controls: list = []
        for month in range(self.m1, self.m2):
            month_label = Text(
                f"{calendar.month_name[month]} {self.current_year}",
                size=30,
                weight=ft.FontWeight.BOLD,
                color="#5A3E2A",
                text_align=ft.TextAlign.CENTER,
            )
            month_matrix=calendar.monthcalendar(self.current_year, month)
            month_grid = Column(alignment=MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0)
            month_grid.controls.append(
                Row(alignment=MainAxisAlignment.SPACE_BETWEEN, controls=[
                    IconButton(icon = icons.CHEVRON_LEFT, on_click=lambda e: self._change_month(-1), icon_color="#5A3E2A", icon_size=50),
                    month_label,
                    IconButton(icon = icons.CHEVRON_RIGHT, on_click=lambda e: self._change_month(1), icon_color="#5A3E2A", icon_size=50),
                ], width=400)
            )
            weekday_labels = [
                Container(
                    border=border.all(0.5, Colors.WHITE),
                    width=120,
                    height=62,
                    bgcolor= "#5A3E2A",
                    alignment=alignment.center,
                    content=Text(
                        weekday,
                        size=20,
                        color= "white",
                        weight= ft.FontWeight.BOLD,
                    )
                )
                for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            ]
            weekday_row = Row(controls=weekday_labels, spacing=0)
            # weekday_row = weekday_labels
            month_grid.controls.append(weekday_row)

            year_month = str(self.current_year) + "-" + str(self.m1)
            jadwal_perawatan_controller = JadwalPerawatanController()
            jadwal_perawatan = jadwal_perawatan_controller.get_all_jadwal_perawatan_by_month(year_month)
            # tanggal = jadwal_perawatan[5].split(" ")[0]
            # hari = tanggal.split("-")[2]
            idx = 0
            max_weeks = 6
            for week in range(max_weeks):
                week_container = Row(spacing=0)
                if week < len(month_matrix):
                    for day in month_matrix[week]:
                        if day == 0:
                            day_container = Container(width=120, height=62, bgcolor="#E0E0E0",border=border.all(0.5, "brown"),)
                        else:
                            day_container = Container(
                                width=120,
                                height=62,
                                bgcolor="white",
                                border=border.all(0.5, "brown"),
                                alignment=alignment.center,
                                data=datetime.date(year=self.current_year, month=month, day=day),
                                on_click=lambda e: self.one_click_date(e),
                            )
                        # day_label = Text(str(day), size=12, color="black")
                        # print(day)
                        if day == 0:
                            day_label = Text("")  # Empty cell for padding
                        elif (day == datetime.date.today().day
                            and month == datetime.date.today().month
                            and self.current_year == datetime.date.today().year):
                            if(idx < len(jadwal_perawatan)):
                                tanggal = jadwal_perawatan[idx][5].split(" ")[0]
                                hari = tanggal.split("-")[2]
                                if(day == int(hari)):
                                    self.page.session.set(str(day), 1)
                                    day_label = self.create_circle2(day, "#AFC9AB")
                                    idx += 1
                                else:
                                    day_label = self.create_circle2(day, "white")
                            else:
                                day_label = self.create_circle2(day, "white")
                            # print("MASUK")

                        elif self.notes.get(self.selected_date) is not None:
                            # print("MASUK2")
                            day_label = self.create_circle(day, "#5F9356")
                        else:
                            if(idx < len(jadwal_perawatan)):
                                tanggal = jadwal_perawatan[idx][5].split(" ")[0]
                                hari = tanggal.split("-")[2]
                                if(day == int(hari)):
                                    self.page.session.set(str(day), 1)
                                    day_label = self.create_circle(day, "#AFC9AB")
                                    idx += 1
                                else:
                                    day_label = self.create_circle(day, "white")
                            else:
                                day_label = self.create_circle(day, "white")
                        day_container.content = day_label
                        week_container.controls.append(day_container)
                else:
                    # Add empty week rows to maintain height
                    for _ in range(7):
                        week_container.controls.append(Container(width=120, height=62))
                month_grid.controls.append(week_container)

            self.calendar_grid.controls.append(month_grid)
        return self.calendar_grid


    def build(self):
    # Notes Display
        day_name = datetime.datetime.now().strftime("%A")
        self.dateToday = Container(
            
            content=Text(
                # bgcolor="#5F9356"
                f"\t{day_name}, \n\t{datetime.date.today().month} {self.current_year}",
                size=14,
                weight="white",
            ),
            bgcolor="#5F9356",
            width=900,
            height=50
        )
        self.notes_display = Container(
            content=Text("No notes for this date.", size=12, color="black"),
            bgcolor="white",
            padding=10,
            width=900,
            height=200,
        )

        # Add Padding to the Calendar
        calendar_with_padding = Container(
            padding=padding.symmetric(horizontal=10),
            content=self.create_month_calendar(self.current_year),
        )
        
        # Structure Everything in a Column
        return Column(
                controls=[
                    calendar_with_padding,
                ],
                # spacing=20,
            )

def calendarBody(page: Page, on_date_selected=None):
    calendar = SetCalendar(on_date_selected=on_date_selected)
    return calendar
