import pytest

from um import count


def test_um_alone():
    assert count("um") == 1
    assert count("um, um, um") == 3
    assert count("hello, um, world") == 1


def test_um_as_substring():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("rum") == 0

def test_um_case_insensitive():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("UM, um, UM") == 3
