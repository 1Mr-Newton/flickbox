import re
import flet as ft
from typing import Callable, List, Dict, Union, Pattern


class Home(ft.View):

    def __init__(self, **kwargs):
        super().__init__(route="/home")

        self.appbar = ft.AppBar(
            bgcolor="#000000",
            title=ft.Text(
                "Home",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),
        )


class Movie(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route="/movie")

        self.appbar = ft.AppBar(
            title=ft.Text("Movie"),
            actions=[ft.IconButton(icon="logout")],
        )

        self.controls = [
            ft.Text(f"Movie:  "),
        ]


class Settings(ft.View):

    def __init__(self, **kwargs):
        super().__init__(route="/settings")

        self.appbar = ft.AppBar(
            title=ft.Text("Settings"),
            actions=[ft.IconButton(icon="logout")],
        )

        self.controls = [
            ft.Text("Settings"),
        ]


class Route:
    def __init__(self, path: str, view: ft.View) -> None:
        self.path: str = path
        self.view: ft.View = view
        self.pattern = (
            re.compile(
                self._convert_path_to_regex(path),
            )
            if ":" in path
            else path
        )

    def _convert_path_to_regex(self, path: str) -> str:
        return re.sub(r":(\w+)", r"(?P<\1>[^/]+)", path)


class Router:
    def __init__(self, page, routes: List[Route]) -> None:
        self.routes: List[Route] = routes

    # def handle_route_change(self, route: str) -> ft.View:
    #     for r in self.routes:
    #         if isinstance(r.pattern, Pattern):
    #             match = r.pattern.match(route)
    #             if match:
    #                 return r.view(**match.groupdict())
    #         elif r.path == route:
    #             return r.view()
    #     return ft.View(route="/404", controls=[ft.Text("404 Not Found")])
    def push(self, route: Route) -> None:
        self.routes.append(route)


router = Router(
    page=ft.Page,
    routes=[
        Route(path="/dashboard", view=Home),
        Route(path="/movie/:id", view=Movie),
        Route(path="/movie/:author/:movie_id", view=Movie),
    ],
)


print(router.handle_route_change("/dashboard"))
# print(router.handle_route_change("/movie/123"))
# print(router.handle_route_change("/movie/john_doe/456"))
