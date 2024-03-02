import flet as ft


class MovieLabel(ft.Row):
    def __init__(self):
        super().__init__()
        self.spacing = 0
        self.controls = [
            ft.Text("IMDB: 7.5", color="#ffffff"),
            ft.Container(width=5),
            ft.Text("2020", color="#ffffff"),
            ft.Container(width=5),
            ft.Text("1h 38m", color="#ffffff"),
            ft.Container(width=5),
            ft.Text("HD", color="#ffffff"),
        ]
