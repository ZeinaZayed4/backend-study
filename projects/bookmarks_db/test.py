import pytest
from bookmark_manager import BookmarkManager
from database_setup import create_bookmarks_table


@pytest.fixture
def manager():
    create_bookmarks_table("test_bookmarks_db")

    m = BookmarkManager(dbname="test_bookmarks_db")
    yield m

    m.close()


def test_add_bookmark(manager):
    assert manager.add_bookmark("https://python.org", "Python Docs") == True


def test_get_bookmarks(manager):
    manager.add_bookmark("https://python.org", "Python Docs")
    manager.add_bookmark("https://google.com", "Google")

    assert len(manager.get_all_bookmarks()) == 2


def test_search_bookmarks(manager):
    manager.add_bookmark("https://python.org", "Python Docs")
    manager.add_bookmark("https://google.com", "Google")

    bookmarks = manager.search_bookmarks("python")
    assert len(bookmarks) == 1
    assert "python" in bookmarks[0][2].lower()


def test_delete_bookmark(manager):
    manager.add_bookmark("https://python.org", "Python Docs")
    result = manager.delete_bookmark("https://python.org")

    assert result is True
    assert len(manager.get_all_bookmarks()) == 0


def test_increment_visits(manager):
    manager.add_bookmark("https://google.com", "Google")
    manager.increment_visits("https://google.com")

    bookmark = manager.search_bookmarks("google")[0]
    assert bookmark[3] == 1


def test_get_stats(manager):
    manager.add_bookmark("https://python.org", "Python Docs")
    manager.add_bookmark("https://google.com", "Google")
    manager.increment_visits("https://google.com")

    assert manager.get_stats() == {
        "total": 2,
        "most_visited": {"title": "Google", "visits": 1},
        "last_created": "Google",
    }
