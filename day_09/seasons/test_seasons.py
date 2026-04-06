import pytest

from seasons import get_minutes, minutes_to_words
from datetime import date

def test_zero_minutes():
    assert get_minutes(date(2026, 4, 6), date(2026, 4, 6)) == 0


def test_one_day():
    assert get_minutes(date(2026, 4, 5), date(2026, 4, 6)) == 1440


def test_one_year():
    assert get_minutes(date(2025, 4, 6), date(2026, 4, 6)) == 525600


def test_leap_year():
    assert get_minutes(date(2024, 2, 1), date(2025, 2, 1)) == 527040


def test_future_date():
    with pytest.raises(ValueError):
        get_minutes(date(2026, 4, 7), date(2026, 4, 6))


def test_minutes_to_words_simple():
    assert minutes_to_words(1440) == "One thousand, four hundred forty minutes"


def test_minutes_to_words_no_and():
    assert " and " not in minutes_to_words(525600)

