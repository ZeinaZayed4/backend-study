import pytest

from twttr import shorten


def test_none_vowel():
    assert shorten("Fly") == "Fly"


def test_lower_vowel():
    assert shorten("twitter") == "twttr"
    

def test_upper_vowel():
    assert shorten("TwIttEr") == "Twttr"


def test_numbers():
    assert shorten("Ca1t") == "C1t"


def test_punctuation():
    assert shorten("What's your word?") == "Wht's yr wrd?"
