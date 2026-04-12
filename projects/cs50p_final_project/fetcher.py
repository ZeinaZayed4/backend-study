import requests
import validators
from bs4 import BeautifulSoup


class FetchError(Exception):
    pass


class Fetcher:
    def __init__(self, url: str):
        self.url = url
        self._response = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url: str):
        if not validators.url(url):
            raise ValueError("Invalid URL")
        self._url = url

    def fetch(self) -> requests.Response:
        if self._response is None:
            try:
                headers = {"User-Agent": "Mozilla/5.0"}
                response = requests.get(self.url, headers=headers, timeout=5)
                response.raise_for_status()
                self._response = response
            except requests.exceptions.RequestException as e:
                raise FetchError(f"Request failed: {e}")
        return self._response

    @property
    def title(self) -> str:
        response = self.fetch()
        soup = BeautifulSoup(response.text, "html.parser")
        if title := soup.find("title"):
            return title.get_text(strip=True)

        for prop in ["og:title", "og:site_name"]:
            if meta := soup.find("meta", property=prop):
                return meta.get("content")

        return "No title"
