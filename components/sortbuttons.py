import flet as ft

from constants.colors import Colors


class SortButtons(ft.Container):
    def __init__(self):
        super().__init__()
        self.padding = ft.padding.only(bottom=16)
        self.content = ft.Container(
            bgcolor=Colors.DARK_PRIMARY,
            padding=ft.padding.symmetric(horizontal=16, vertical=8),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=40,
                        width=100,
                        border=ft.border.all(1.5, "white"),
                        border_radius=ft.border_radius.all(20),
                        padding=ft.padding.symmetric(
                            horizontal=8,
                            vertical=4,
                        ),
                        content=ft.Text(
                            "Series",
                            color="white",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        height=40,
                        width=100,
                        border=ft.border.all(1.5, "white"),
                        border_radius=ft.border_radius.all(20),
                        padding=ft.padding.symmetric(
                            horizontal=8,
                            vertical=4,
                        ),
                        content=ft.Text(
                            "Movies",
                            color="white",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        height=40,
                        width=100,
                        border=ft.border.all(1.5, "white"),
                        border_radius=ft.border_radius.all(20),
                        padding=ft.padding.symmetric(
                            horizontal=8,
                            vertical=4,
                        ),
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    "Genres",
                                    color="white",
                                    text_align=ft.TextAlign.CENTER,
                                ),
                                ft.Icon(
                                    ft.icons.ARROW_DROP_DOWN,
                                    color="white",
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
