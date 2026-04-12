import os
import requests
from bs4 import BeautifulSoup
from fetcher import Fetcher


class Scraper:
    def __init__(self, fetcher: Fetcher):
        self.fetcher = fetcher

    def _extract_content(self) -> str:
        response = self.fetcher.fetch()
        soup = BeautifulSoup(response.text, "html.parser")
        parts = []

        if desc := soup.find("meta", attrs={"name": "description"}):
            parts.append(desc.get("content", ""))
        if kw := soup.find("meta", attrs={"name": "keywords"}):
            parts.append(kw.get("content", ""))
        for tag in soup.find_all(["h1", "h2"])[:4]:
            parts.append(tag.get_text(strip=True))
        
        return " ".join(parts)
    
    def suggest_tags(self) -> list[str]:
        try:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                return []
            
            content = self._extract_content()

            response = requests.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json"
                },
                json={
                    "model": "claude-sonnet-4-20250514",
                    "max_tokens": 100,
                    "messages": [
                        {
                            "role": "user",
                            "content": f"Suggest 3-5 short lowercase tags for this webpage content. Reply with only a comma separated list, nothing else.\n\n{content}"
                        }
                    ]
                }
            )

            result = response.json()
            tags_string = result["content"][0]["text"]
            return [tag.strip() for tag in tags_string.split(",")]
        except Exception:
            return []
