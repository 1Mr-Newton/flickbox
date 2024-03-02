import re
from typing import Any, Dict
from routes.routes import Routes
from screens.home import Home
from screens.movie import Movie
from screens.settings import Settings
import flet as ft


ROUTER = {
    Routes.DASHBOARD_ROUTE: Home,
    Routes.SETTINGS_ROUTE: Settings,
    re.compile(r"/movie/(?P<id>\d+)"): Movie,
    Routes.NOT_FOUND_ROUTE: "404 Not Found",
}


def dynamic_router(path: str):
    for route, screen in ROUTER.items():
        if route == path:
            return screen
        if isinstance(route, re.Pattern):
            match = route.match(path)
            if match:
                return screen
    return None
