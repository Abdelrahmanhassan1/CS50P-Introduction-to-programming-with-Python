from numb3rs import validate


def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("210.22.28.10") == True
    assert validate("192.186.1.1") == True


def test_not_valid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False


def test_first_byte():
    assert validate("1000.20.30.10") == False
    assert validate("512.210.30.50") == False
