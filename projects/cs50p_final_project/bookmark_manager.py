import csv
import difflib
import webbrowser
from bookmark import Bookmark
from datetime import datetime
from typing import Optional


class BookmarkManager:
    def __init__(self, file_name="bookmarks.csv"):
        self.file_name = file_name

    def _load(self):
        try:
            with open(self.file_name) as file:
                reader = csv.DictReader(file)
                return [Bookmark.from_dict(row) for row in reader]
        except FileNotFoundError:
            return []

    def _save(self, bookmarks):
        fieldnames = ["url", "title", "tags", "visits", "created_at", "last_opened"]
        with open(self.file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(b.to_dict() for b in bookmarks)

    def all(self):
        return self._load()

    def add(self, bookmark: Bookmark) -> None:
        bookmarks = self._load()
        for b in bookmarks:
            if b.url == bookmark.url:
                raise ValueError("\nBookmark already exists")

        bookmarks.append(bookmark)
        self._save(bookmarks)

    def delete(self, url: str) -> None:
        bookmarks = self._load()
        retained_bookmarks = [b for b in bookmarks if url != b.url]

        if len(bookmarks) == len(retained_bookmarks):
            raise ValueError(f"\nNo bookmark found with URL: {url}")

        self._save(retained_bookmarks)

    def find(self, url: str) -> Optional[Bookmark]:
        bookmarks = self._load()

        for b in bookmarks:
            if url == b.url:
                return b
        return None

    def update(self, bookmark: Bookmark) -> None:
        bookmarks = self._load()

        for i, b in enumerate(bookmarks):
            if bookmark.url == b.url:
                bookmarks[i] = bookmark
                self._save(bookmarks)
                return
        raise ValueError(f"\nNo bookmark found with URL: {bookmark.url}")

    def open_bookmark(self, url: str) -> None:
        if bookmark := self.find(url):
            bookmark.visits += 1
            bookmark.last_opened = datetime.now()
            self.update(bookmark)
            webbrowser.open_new_tab(url)
        else:
            raise ValueError(f"\nNo bookmark found with URL: {url}")

    def stats(self) -> dict:
        bookmarks = self._load()
        if not bookmarks:
            return {}

        total = len(bookmarks)
        most_visited = max(bookmarks, key=lambda b: b.visits)

        tag_counts = {}
        for b in bookmarks:
            for tag in b.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        top_tags = sorted(tag_counts.items(), key=lambda t: t[1], reverse=True)[:3]

        recently_added = max(bookmarks, key=lambda b: b.created_at)

        return {"total": total, "most_visited": most_visited, "top_tags": top_tags, "recently_added": recently_added}

    def search(self, query: str) -> list[Bookmark]:
        query = query.lower().strip()
        bookmarks = self._load()

        exact = [b for b in bookmarks if self._matches_exact(b, query)]
        if exact:
            return exact

        results = [b for b in bookmarks if self._score(b, query) > 0.6]
        results.sort(key=lambda b: self._score(b, query), reverse=True)
        return results

    def _matches_exact(self, bookmark: Bookmark, query: str) -> bool:
        return query == bookmark.title.lower() or query in [
            t.lower() for t in bookmark.tags
        ]

    def _score(self, bookmark: Bookmark, query: str) -> float:
        title = bookmark.title.lower()

        if query in title:
            return 1.0
        
        title_score = difflib.SequenceMatcher(None, query, title).ratio()
        tag_score = max(
            (
                difflib.SequenceMatcher(None, query, tag).ratio()
                for tag in bookmark.tags
            ),
            default=0,
        )
        return max(title_score, tag_score)
