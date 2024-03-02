import flet as ft

from constants.colors import Colors

urls = [
    "https://static.fmovies.cab/images/m/chrhktVJwI6Td_3RF1alBiyazwBbNh_tIaMh7KQQo1kNjWBxD4_tTZZzzbub2JerFKKCpk6auU_1mjXcuERYJtOXFsQ8GFEOf3On_DfKeSY.jpg?1",
    "https://static.fmovies.cab/images/m/SpnJisZNEK_fh_6PYy0riAZlTmO16iZAHqqO3t7HuSclpMVoD8wR8tGPiExPOq-ZEpNhgAi3QM8yA55w6eoO3vsB2wI7kjS-MbK9Zrlorb8.jpg?1",
]


class Carousel(ft.Container):
    def __init__(self):
        super().__init__()
        self.height = 500
        self.width = 350
        self.border_radius = 20
        self.clip_behavior = ft.ClipBehavior.ANTI_ALIAS
        self.featuredImageRef = ft.Ref()
        self.urls = urls
        self.current_index = 0
        self.bgcolor = "white"
        self.padding = 1
        self.content = ft.Container(
            border_radius=20,
            expand=True,
            width=350,
            bgcolor=Colors.DARK_PRIMARY,
            content=ft.GestureDetector(
                width=350,
                content=ft.Image(
                    ref=self.featuredImageRef,
                    src=self.urls[self.current_index],
                    fit=ft.ImageFit.COVER,
                    border_radius=20,
                ),
                on_horizontal_drag_end=self.update_image,
            ),
        )

    def update_image(self, e):
        self.current_index = (self.current_index + 1) % len(self.urls)
        self.featuredImageRef.current.src = self.urls[self.current_index]
        self.featuredImageRef.current.update()
