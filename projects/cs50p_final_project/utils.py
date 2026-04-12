from bookmark import Bookmark


def display_bookmarks(bookmarks: list[Bookmark]):
    if not bookmarks:
        print("\nNo bookmarks found")
        return

    print(f"\n- Your Bookmarks ({len(bookmarks)} total):")
    print("------------------------------------")
    for i, b in enumerate(bookmarks):
        formatted_tags = " ".join(f"#{tag}" for tag in b.tags) or "No tags"
        last_opened = b.last_opened.strftime("%Y-%m-%d") if b.last_opened else "Never"

        print(f"[{i + 1}] {b.title}")
        print(f"    URL: {b.url}")
        print(f"    Tags: {formatted_tags}")
        print(f"    Visits: {b.visits} | Last opened: {last_opened}")


def display_search_results(bookmarks: list[Bookmark]):
    if not bookmarks:
        print("\nNo bookmarks found")
        return

    print(f"\n- Results ({len(bookmarks)} found):")
    for i, b in enumerate(bookmarks):
        formatted_tags = " ".join(f"#{tag}" for tag in b.tags) or "No tags"
        print(f"[{i + 1}] {b.title}")
        print(f"    {formatted_tags}")


def display_stats(stats: dict):
    if not stats:
        print("\nNo bookmarks found")
        return

    print("\n- Your Stats:")
    print("---------------------")
    print(f" - Total bookmarks: {stats["total"]}")
    print(" - Most visited: ")
    print(
        f"    -> {stats["most_visited"].title} ({stats["most_visited"].visits} visits)"
    )
    print(" - Top tags:")
    for tag, freq in stats["top_tags"]:
        print(f"    #{tag} ({freq})")

    print(f" - Recently added: {stats['recently_added'].title}")

def display_menu():
    print("\n- CLI Bookmark Manager")
    print("------------------------")
    print("1. Add Bookmark")
    print("2. View bookmarks")
    print("3. Search")
    print("4. Open Bookmark")
    print("5. Delete Bookmark")
    print("6. Stats")
    print("7. Exit")
