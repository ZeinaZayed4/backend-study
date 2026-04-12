import pytest
from bookmark_manager import BookmarkManager
from bookmark import Bookmark


def make_manager(tmp_path):
    return BookmarkManager(file_name=str(tmp_path / "test.csv"))


def make_bookmark(url="https://example.com", title="Example"):
    return Bookmark(url=url, title=title)


def test_add(tmp_path):
    manager = make_manager(tmp_path)
    manager.add(make_bookmark())

    assert len(manager.all()) == 1


def test_add_duplicate(tmp_path):
    manager = make_manager(tmp_path)
    manager.add(make_bookmark())

    with pytest.raises(ValueError):
        manager.add(make_bookmark())


def test_delete(tmp_path):
    manager = make_manager(tmp_path)
    manager.add(make_bookmark())
    manager.delete("https://example.com")
    assert manager.all() == []


def test_delete_missing(tmp_path):
    manager = make_manager(tmp_path)
    with pytest.raises(ValueError):
        manager.delete("https://example.com")


def test_find(tmp_path):
    manager = make_manager(tmp_path)
    manager.add(make_bookmark())
    assert manager.find("https://example.com") != None


def test_find_missing(tmp_path):
    manager = make_manager(tmp_path)
    assert manager.find("https://example.com") == None


def test_search(tmp_path):
    manager = make_manager(tmp_path)
    manager.add(make_bookmark(title="CS50P - Programming With Python"))
    assert len(manager.search("python")) == 1
