import pytest
from bookmark import Bookmark
from datetime import datetime

sample = {
    "url": "https://example.com",
    "title": "Example",
    "tags": "python,web",
    "visits": "3",
    "created_at": "2026-01-01 12:00:00",
    "last_opened": "Never",
}


def make_bookmark(**kwargs):
    defaults = dict(url="https://example.com", title="Example")
    return Bookmark(**{**defaults, **kwargs})


def test_valid_url():
    make_bookmark()


def test_invalid_url():
    with pytest.raises(ValueError):
        Bookmark(url="test", title="Test")


def test_to_dict_keys():
    result = make_bookmark().to_dict()
    assert set(result.keys()) == {
        "url",
        "title",
        "tags",
        "visits",
        "created_at",
        "last_opened",
    }


def test_to_dict_last_opened_none():
    result = make_bookmark().to_dict()
    assert result["last_opened"] == "Never"


def test_from_dict_types():
    result = Bookmark.from_dict(sample)
    assert isinstance(result.visits, int)
    assert isinstance(result.tags, list)
    assert isinstance(result.created_at, datetime)


def test_round_trip():
    time = datetime(2026, 4, 11, 12, 0, 0)
    result = make_bookmark(created_at=time)
    assert Bookmark.from_dict(result.to_dict()) == result
