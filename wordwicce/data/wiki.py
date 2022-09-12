import requests

from bs4 import BeautifulSoup
from discord import Colour, Embed
from urllib.parse import quote_plus


WIKI_COLOUR = Colour.from_rgb(202, 77, 77)


class WikiExcerpt:
    def __init__(self, title: str, text: str, url: str, picture: str | None = None):
        self.title = title
        self.text = text
        self.url = url
        self.picture = picture

    def to_embed(self) -> Embed:
        embed = Embed(
            title=self.title, description=self.text, url=self.url, colour=WIKI_COLOUR
        )
        if self.picture:
            embed.set_image(url=self.picture)
        return embed


class Wiki:
    BASE_URL = "https://anglosaxonheathenry.wiki"

    def normalize_query(self, query: str) -> str:
        return quote_plus(query.capitalize())

    def request(self, query: str) -> str | None:
        query = self.normalize_query(query)
        r = requests.get(f"{self.BASE_URL}/{query}")
        if r.status_code != 200:
            return None
        return r.text

    def search(self, query: str) -> WikiExcerpt | None:
        response = self.request(query)
        if not response:
            return None
        soup = BeautifulSoup(response, "html.parser")
        title = soup.head.find("meta", property="og:title")
        text = soup.head.find("meta", property="og:description")
        url = soup.head.find("meta", property="og:url")
        picture = soup.head.find("meta", property="og:image")
        if text is None or title is None or url is None:
            return None
        return WikiExcerpt(
            title.attrs["content"],
            text.attrs["content"],
            url.attrs["content"],
            picture.attrs["content"] if picture is not None else None,
        )
