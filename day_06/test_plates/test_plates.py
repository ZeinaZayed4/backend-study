from plates import is_valid


def test_length():
    assert is_valid("I") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("HEY") == True


def test_first_two_letters():
    assert is_valid("I2") == False
    assert is_valid("2I") == False
    assert is_valid("IN") == True


def test_numbers():
    assert is_valid("ZZZ02") == False
    assert is_valid("ZZZ20Z") == False
    assert is_valid("ZZZ20") == True


def test_none_alphanumeric():
    assert is_valid("HE!LO") == False
    assert is_valid("HEL.O") == False
    assert is_valid("HELLO") == True


def test_alphanumeric():
    assert is_valid("AAA20") == True
    assert is_valid("AAAA2") == True
