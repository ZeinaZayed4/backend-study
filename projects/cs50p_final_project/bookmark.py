import validators
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Bookmark:
    url: str
    title: str
    tags: list[str] = field(default_factory=list)
    visits: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    last_opened: Optional[datetime] = None

    @classmethod
    def from_dict(cls, data):
        last_opened = data["last_opened"]
        return cls(
            url=data["url"],
            title=data["title"],
            tags=data["tags"].split(",") if data["tags"] else [],
            visits=int(data["visits"]),
            created_at=datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S"),
            last_opened=(
                None
                if last_opened in ("Never", "", None)
                else datetime.strptime(last_opened, "%Y-%m-%d %H:%M:%S")
            ),
        )

    def to_dict(self):
        return {
            "url": self.url,
            "title": self.title,
            "tags": ",".join(self.tags),
            "visits": str(self.visits),
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "last_opened": (
                self.last_opened.strftime("%Y-%m-%d %H:%M:%S")
                if self.last_opened
                else "Never"
            ),
        }

    def __post_init__(self):
        if not validators.url(self.url):
            raise ValueError("Invalid URL")
        self.url = self.url.rstrip("/")
