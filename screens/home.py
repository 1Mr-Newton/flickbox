import asyncio
import flet as ft
from api.movieapi import get_home_data
from components.home_category_item import HomeCategoryItem
from components.movie_item import MovieItem
from components.movie_labels import MovieLabel
from components.sortbuttons import SortButtons
from components.ui.carousel import Carousel
from constants.data import CATEGORIZED
from providers.data_provider import DataProvider
from providers.navigator import Navigator
from routes.routes import Routes
from constants.colors import Colors


class Home(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route=Routes.DASHBOARD_ROUTE)
        self.bgcolor = "black"
        self.spacing = 0
        self.padding = 0
        self.scroll = ft.ScrollMode.HIDDEN

        self.appbar = ft.AppBar(
            bgcolor=Colors.DARK_PRIMARY,
            title=ft.Text(
                "FlickBox",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),
            actions=[
                ft.IconButton(
                    icon=ft.icons.SEARCH,
                ),
            ],
        )
        self.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.HOME_OUTLINED,
                    label="Home",
                    selected_icon=ft.icons.HOME,
                ),
                ft.NavigationDestination(
                    icon=ft.icons.MOVIE_OUTLINED,
                    selected_icon=ft.icons.MOVIE,
                    label="New & Hot",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS,
                    label="Settings",
                ),
            ]
        )

        asyncio.run(self._mount())
        self.controls = [
            SortButtons(),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    Carousel(),
                ],
            ),
            ft.Container(height=10),
            ft.Column(
                controls=[
                    HomeCategoryItem(
                        title=category["title"],
                        movies=category["data"],
                    )
                    for category in CATEGORIZED
                ]
            ),
        ]

    async def _mount(self):
        self.home_data = await get_home_data()
