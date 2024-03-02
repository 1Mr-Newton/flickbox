from urllib.parse import parse_qs, urlparse
import flet as ft
from helpers.param_converter import convert_params
from providers.navigator import Navigator
from routes.router import ROUTER, dynamic_router
from routes.routes import Routes
import sys


class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        page.window_height = 850
        page.window_width = 400
        page.padding = 0

        Navigator.update_page(page)
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.views.clear()

        Navigator.replace(Routes.DASHBOARD_ROUTE)
        # Navigator.push(Routes.MOVIE_ROUTE.format(id=455))

    def route_change(self, route: ft.RouteChangeEvent):
        _route = urlparse(route.route)
        params = parse_qs(_route.query)
        path = _route.path

        params["route"] = [path]
        params = convert_params(params)

        new_view = dynamic_router(path)

        clear = params.get("clear", False)

        if clear:
            self.page.views.clear()

        if not new_view:
            Navigator.replace(Routes.NOT_FOUND_ROUTE)

        elif len(self.page.views) == 0:
            self.page.views.append(new_view(**params))

        elif self.page.views[-1].route != new_view(**params).route:
            self.page.views.append(new_view(**params))

    def view_pop(self, event: ft.ViewPopEvent):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


ft.app(Main, assets_dir="assets")
