import pytest

from numb3rs import validate


def test_valid():
    assert validate("172.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("172.168.1.0") == True
    assert validate("0.0.0.0") == True


def test_invalid_out_of_range():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False


def test_invalid_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("01.0.0.1") == False


def test_invalid_not_an_address():
    assert validate("cat") == False
    assert validate("") == False
    assert validate("1.2.3.4.5") == False
    assert validate("-1.0.0.1") == False


def test_invalid_non_dot_separator():
    assert validate("1.2.3F4") == False
    assert validate("1.2.3 4") == False
    assert validate("1.2F3.4") == False
