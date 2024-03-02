import flet as ft
from components.movie_labels import MovieLabel

from providers.navigator import Navigator
from routes.routes import Routes


class MovieItem(ft.Container):
    def __init__(self, cover_url, title, genre):
        super().__init__()
        self.cover_url = cover_url
        self.title = title
        self.genre = genre
        self.height = 150
        self.width = 100
        self.content = ft.Image(
            src=self.cover_url,
            border_radius=10,
            fit=ft.ImageFit.COVER,
        )
        self.on_click = lambda _: Navigator.push(Routes.MOVIE_ROUTE.format(id=500))
