import flet as ft
from components.movie_item import MovieItem
from components.movie_labels import MovieLabel
from providers.data_provider import DataProvider
from routes.routes import Routes


sample_media = [
    ft.VideoMedia(
        "https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4"
    ),
    ft.VideoMedia(
        "https://user-images.githubusercontent.com/28951144/229373718-86ce5e1d-d195-45d5-baa6-ef94041d0b90.mp4"
    ),
    ft.VideoMedia(
        "https://user-images.githubusercontent.com/28951144/229373716-76da0a4e-225a-44e4-9ee7-3e9006dbc3e3.mp4"
    ),
    ft.VideoMedia(
        "https://user-images.githubusercontent.com/28951144/229373695-22f88f13-d18f-4288-9bf1-c3e078d83722.mp4"
    ),
    ft.VideoMedia(
        "https://user-images.githubusercontent.com/28951144/229373709-603a7a89-2105-4e1b-a5a5-a6c3567c9a59.mp4",
        extras={
            "artist": "Thousand Foot Krutch",
            "album": "The End Is Where We Begin",
        },
        http_headers={
            "Foo": "Bar",
            "Accept": "*/*",
        },
    ),
]


a = (
    ft.Container(
        blur=40,
        width=500,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                # ft.Video(
                #     playlist=sample_media[0:2],
                #     playlist_mode=ft.PlaylistMode.LOOP,
                #     aspect_ratio=16 / 9,
                #     volume=100,
                #     autoplay=False,
                #     filter_quality=None,
                #     muted=False,
                # ),
                ft.Container(width=500, height=300, bgcolor="#8b8b8b"),
                ft.Container(
                    padding=ft.padding.symmetric(horizontal=5),
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        spacing=0,
                        controls=[
                            MovieLabel(),
                            ft.Container(height=10),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        padding=ft.padding.symmetric(vertical=5),
                                        content=ft.Row(
                                            spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.PLAY_ARROW,
                                                    color="black",
                                                    size=24,
                                                ),
                                                ft.Text(
                                                    "Watch",
                                                    color="black",
                                                    weight=ft.FontWeight.BOLD,
                                                    size=16,
                                                ),
                                            ],
                                        ),
                                        expand=True,
                                        bgcolor="white",
                                    )
                                ]
                            ),
                            ft.Container(height=10),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        padding=ft.padding.symmetric(vertical=5),
                                        content=ft.Row(
                                            spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Icon(
                                                    ft.icons.ADD,
                                                    color="white",
                                                    size=24,
                                                ),
                                                ft.Text(
                                                    "Save",
                                                    color="white",
                                                    weight=ft.FontWeight.BOLD,
                                                    size=16,
                                                ),
                                            ],
                                        ),
                                        expand=True,
                                        bgcolor="#292929",
                                    )
                                ]
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                "Aquaman balances his duties as king and as a member of the Justice League, all while planning a wedding. Black Manta is on the hunt for Atlantean tech to help rebuild his armor. Orm plots to escape his Atlantean prison.",
                                size=12,
                                color="white",
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                "Cast: ",
                                size=12,
                                color="#c8c8c8",
                                spans=[
                                    ft.TextSpan(
                                        "Jason Momoa, Amber Heard, Willem Dafoe, Patrick Wilson, Dolph Lundgren, Yahya Abdul-Mateen II, Nicole Kidman, Ludi Lin, Temuera Morrison, Randall Park, Graham McTavish, Michael Beach, Leigh Whannell, Julie Andrews",
                                        style=ft.TextStyle(color="#747474"),
                                    )
                                ],
                            ),
                            ft.Text(
                                "Director: ",
                                size=12,
                                color="#c8c8c8",
                                spans=[
                                    ft.TextSpan(
                                        "James Wan",
                                        style=ft.TextStyle(color="#747474"),
                                    )
                                ],
                            ),
                            ft.Container(height=15),
                            ft.Text(
                                value="More like this",
                                size=18,
                                color="white",
                                weight=ft.FontWeight.W_600,
                            ),
                            ft.Container(height=15),
                            ft.GridView(
                                expand=True,
                                runs_count=5,
                                max_extent=150,
                                child_aspect_ratio=0.7,
                                spacing=5,
                                run_spacing=5,
                                controls=[
                                    ft.Container(expand=1, bgcolor="#8b8b8b"),
                                    ft.Container(expand=1, bgcolor="#8b8b8b"),
                                    ft.Container(expand=1, bgcolor="#8b8b8b"),
                                    ft.Container(expand=1, bgcolor="#8b8b8b"),
                                    ft.Container(expand=1, bgcolor="#8b8b8b"),
                                    ft.Container(expand=1, bgcolor="#8b8b8b"),
                                    ft.Container(expand=1, bgcolor="#8b8b8b"),
                                ],
                            ),
                        ],
                    ),
                ),
            ],
        ),
    ),
)


class Movie(ft.View):
    def __init__(self, route, **kwargs):
        super().__init__(route=route)
        self.appbar = ft.AppBar(
            # title=ft.Text("Settings"),
        )
        self.padding = 0
        self.spacing = 0
        # self.scroll = ft.ScrollMode.AUTO
        self.expand = True

        self.controls = [
            ft.Container(height=300, bgcolor="green"),
            ft.Container(
                expand=True,
                content=ft.Column(
                    scroll=ft.ScrollMode.HIDDEN,
                    spacing=0,
                    controls=[
                        MovieLabel(),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    padding=ft.padding.symmetric(vertical=5),
                                    content=ft.Row(
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Icon(
                                                ft.icons.PLAY_ARROW,
                                                color="black",
                                                size=24,
                                            ),
                                            ft.Text(
                                                "Watch",
                                                color="black",
                                                weight=ft.FontWeight.BOLD,
                                                size=16,
                                            ),
                                        ],
                                    ),
                                    expand=True,
                                    bgcolor="white",
                                )
                            ]
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    padding=ft.padding.symmetric(vertical=5),
                                    content=ft.Row(
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.Icon(
                                                ft.icons.ADD,
                                                color="white",
                                                size=24,
                                            ),
                                            ft.Text(
                                                "Save",
                                                color="white",
                                                weight=ft.FontWeight.BOLD,
                                                size=16,
                                            ),
                                        ],
                                    ),
                                    expand=True,
                                    bgcolor="#292929",
                                )
                            ]
                        ),
                        ft.Container(height=10),
                        ft.Text(
                            "Aquaman balances his duties as king and as a member of the Justice League, all while planning a wedding. Black Manta is on the hunt for Atlantean tech to help rebuild his armor. Orm plots to escape his Atlantean prison.",
                            size=12,
                            color="white",
                        ),
                        ft.Container(height=10),
                        ft.Text(
                            "Cast: ",
                            size=12,
                            color="#c8c8c8",
                            spans=[
                                ft.TextSpan(
                                    "Jason Momoa, Amber Heard, Willem Dafoe, Patrick Wilson, Dolph Lundgren, Yahya Abdul-Mateen II, Nicole Kidman, Ludi Lin, Temuera Morrison, Randall Park, Graham McTavish, Michael Beach, Leigh Whannell, Julie Andrews",
                                    style=ft.TextStyle(color="#747474"),
                                )
                            ],
                        ),
                        ft.Text(
                            "Director: ",
                            size=12,
                            color="#c8c8c8",
                            spans=[
                                ft.TextSpan(
                                    "James Wan",
                                    style=ft.TextStyle(color="#747474"),
                                )
                            ],
                        ),
                        ft.Container(height=15),
                        ft.Text(
                            value="More like this",
                            size=18,
                            color="white",
                            weight=ft.FontWeight.W_600,
                        ),
                        ft.Container(height=15),
                        ft.GridView(
                            runs_count=5,
                            max_extent=150,
                            child_aspect_ratio=0.7,
                            spacing=5,
                            run_spacing=5,
                            controls=[
                                MovieItem(
                                    cover_url="https://static.fmovies.cab/images/m/SpnJisZNEK_fh_6PYy0riAZlTmO16iZAHqqO3t7HuSclpMVoD8wR8tGPiExPOq-ZEpNhgAi3QM8yA55w6eoO3vsB2wI7kjS-MbK9Zrlorb8.jpg?1",
                                    title="Aquaman",
                                    genre="Action",
                                ),
                                MovieItem(
                                    cover_url="https://static.fmovies.cab/images/m/SpnJisZNEK_fh_6PYy0riAZlTmO16iZAHqqO3t7HuSclpMVoD8wR8tGPiExPOq-ZEpNhgAi3QM8yA55w6eoO3vsB2wI7kjS-MbK9Zrlorb8.jpg?1",
                                    title="Aquaman",
                                    genre="Action",
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        ]
