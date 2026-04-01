import pytest

from fuel import convert, gauge


def test_convert_value_error():
    for value in ["cat/dog", "1.5/3", "5/4", "-2/3"]:
        with pytest.raises(ValueError):
            convert(value)


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
