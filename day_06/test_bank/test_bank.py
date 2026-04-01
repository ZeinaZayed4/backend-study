from bank import value


def test_hello_greeting():
    assert value("hello") == 0
    assert value("Hello, there") == 0


def test_h_greeting():
    assert value("how are you doing?") == 20
    assert value("How are you doing?") == 20


def test_none_h_greeting():
    assert value("What's happening?") == 100
