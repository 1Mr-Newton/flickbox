from typing import List
import flet as ft
from components.movie_item import MovieItem
from constants.colors import Colors


class HomeCategoryItem(ft.Container):
    def __init__(self, title: str, movies: list, **kwargs):
        super().__init__()
        self.title = title

        self.movies = movies
        self.mControls: List[ft.Control] = [
            ft.Column(
                controls=[
                    ft.Text(
                        movie.get("title"),
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=Colors.WHITE,
                    ),
                ]
            )
            for movie in self.movies
        ]
        self.content = ft.ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=True,
            controls=self.mControls,
        )


# a = controls = [
#     ft.Row(
#         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#         controls=[
#             ft.Text(
#                 self.title,
#                 size=20,
#                 weight=ft.FontWeight.BOLD,
#                 color=Colors.WHITE,
#             ),
#         ],
#     ),
#     ft.Row(
#         scroll=ft.ScrollMode.HIDDEN,
#         controls=[
#             MovieItem(
#                 cover_url=movie.get(
#                     "cover_url",
#                 ),
#                 genre=movie.get("genre"),
#                 title=movie.get("name"),
#             )
#             for movie in self.movies
#         ],
#     ),
# ]
