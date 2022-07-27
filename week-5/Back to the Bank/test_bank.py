from bank import value


def test_0():
    assert value("Hello") == 0
    assert value("Hello, Ali") == 0
    assert value("Hello, Madam") == 0
    assert value("Hello, Sir") == 0


def test_20():
    assert value("How you doing?") == 20
    assert value("Hi, How you doing?") == 20


def test_100():
    assert value("Welcome Sir!") == 100
    assert value("What's happening?") == 100
