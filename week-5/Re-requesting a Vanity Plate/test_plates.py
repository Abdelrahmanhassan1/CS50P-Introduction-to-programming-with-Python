from plates import is_valid


def test_valid():
    assert is_valid("cs50") == True
    assert is_valid("ABC123") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("AA") == True


def test_non_valid():
    assert is_valid("cs50p") == False
    assert is_valid("cs05") == False
    assert is_valid('O') == False
    assert is_valid("PI3.14") == False


def test_not_beginning_with_alphebet():
    assert is_valid('123Pi') == False
    assert is_valid('0Hg12') == False
    assert is_valid('87Yu') == False


def test_startwith():
    assert is_valid("1") == False
    assert is_valid("22") == False


def test_letters():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_numbers():
    assert is_valid("123456") == False
    assert is_valid("123ABC") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB12CA") == False


def test_symbols():
    assert is_valid("ABC?!-") == False
    assert is_valid(". 12[]") == False
    assert is_valid("/B^D3*") == False
