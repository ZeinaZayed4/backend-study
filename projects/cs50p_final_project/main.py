from bookmark import Bookmark
from bookmark_manager import BookmarkManager
from fetcher import Fetcher, FetchError
from scraper import Scraper
from utils import display_menu, display_bookmarks, display_search_results, display_stats


def main():
    manager = BookmarkManager()

    while True:
        display_menu()
        try:
            choice = int(input("\n> ").strip())
        except ValueError:
            print("Enter a number")
            continue

        if choice == 1:
            handle_add(manager)
        elif choice == 2:
            handle_view(manager)
        elif choice == 3:
            handle_search(manager)
        elif choice == 4:
            handle_open(manager)
        elif choice == 5:
            handle_delete(manager)
        elif choice == 6:
            handle_stats(manager)
        elif choice == 7:
            print("\nGoodbye!")
            break
        else:
            print("\n Invalid choice, try again")


def handle_view(manager: BookmarkManager):
    display_bookmarks(manager.all())


def handle_stats(manager: BookmarkManager):
    display_stats(manager.stats())


def handle_search(manager: BookmarkManager):
    query = input("\n- Search: ").strip()
    results = manager.search(query)
    display_search_results(results)


def handle_open(manager: BookmarkManager):
    bookmarks = manager.all()
    display_bookmarks(bookmarks)

    try:
        idx = int(input("\n- Enter bookmark ID: ").strip()) - 1
        url = bookmarks[idx].url
        manager.open_bookmark(url)
        print("\n Opened successfully")
    except (ValueError, IndexError):
        print("\n Invalid ID")


def handle_delete(manager: BookmarkManager):
    bookmarks = manager.all()
    display_bookmarks(bookmarks)

    try:
        idx = int(input("\n- Enter bookmark ID: ").strip()) - 1
        url = bookmarks[idx].url
        manager.delete(url)
        print("\n Bookmark deleted")
    except (ValueError, IndexError):
        print("\n Invalid ID")


def handle_add(manager: BookmarkManager):
    url = input("\n- URL: ").strip()
    try:
        fetcher = Fetcher(url)
        title = fetcher.title
    except FetchError as e:
        print(f"\n Couldn't fetch URL: {e}")
        return

    tags = Scraper(fetcher).suggest_tags()

    if tags:
        print(f"- Suggested tags: {' '.join(f'#{t}' for t in tags)}")
        choice = input("Add these tags (yes/no): ").strip().lower()
        if choice == "no":
            tags = input("- Tags (space separated): ").strip().split()
    else:
        tags = input("- Tags (space separated): ").strip().split()

    bookmark = Bookmark(url=url, title=title, tags=tags)
    try:
        manager.add(bookmark)
        print("\n Bookmark saved")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
