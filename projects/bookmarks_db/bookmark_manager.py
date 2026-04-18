from database_connection import DatabaseConnection


class BookmarkManager:
    def __init__(self, dbname="bookmarks_db"):
        self.db = DatabaseConnection(dbname=dbname)

    def add_bookmark(self, url, title=None):
        try:
            self.db.execute(
                "INSERT INTO bookmarks (url, title) VALUES (%s, %s)", (url, title)
            )
            return True
        except Exception as e:
            return f"Error: {e}"

    def get_all_bookmarks(self):
        return self.db.fetch_all(
            "SELECT id, url, title, visits, created_at, updated_at FROM bookmarks ORDER BY created_at DESC"
        )

    def search_bookmarks(self, keyword):
        return self.db.fetch_all(
            "SELECT * FROM bookmarks WHERE title ILIKE %s OR url ILIKE %s",
            (f"%{keyword}%", f"%{keyword}%"),
        )

    def delete_bookmark(self, url):
        try:
            self.db.execute("DELETE FROM bookmarks WHERE url = %s", (url,))
            return True
        except Exception:
            return f"Cannot delete {url}"

    def increment_visits(self, url):
        self.db.execute(
            "UPDATE bookmarks SET visits = visits + 1 WHERE url = %s", (url,)
        )

    def get_stats(self):
        total = self.db.fetch_one("SELECT COUNT(*) FROM bookmarks")[0]
        most_visited = self.db.fetch_one(
            "SELECT title, visits FROM bookmarks ORDER BY visits DESC LIMIT 1"
        )
        last_created = self.db.fetch_one(
            "SELECT title FROM bookmarks ORDER BY created_at DESC LIMIT 1"
        )
        return {
            "total": total,
            "most_visited": (
                {
                    "title": most_visited[0],
                    "visits": most_visited[1],
                }
                if most_visited
                else None
            ),
            "last_created": last_created[0] if last_created else None,
        }

    def close(self):
        self.db.close()
