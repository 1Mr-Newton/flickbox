class MoviePre:
    id: str
    href: str
    name: str
    genre: str
    quality: str
    image: str
    imdb: str
    year: str
    duration: str
    country: str
    description: str

    def __init__(
        self,
        id: str,
        href: str,
        name: str,
        genre: str,
        quality: str,
        image: str,
        imdb: str,
        year: str,
        duration: str,
        country: str,
        description: str,
    ):
        self.id = id
        self.href = href
        self.name = name
        self.genre = genre
        self.quality = quality
        self.image = image
        self.imdb = imdb
        self.year = year
        self.duration = duration
        self.country = country
        self.description = description
