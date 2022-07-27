from twttr import shorten


def test_lowercase():
    assert shorten("hello world") == "hll wrld"
    assert shorten("name is abdo") == "nm s bd"
    assert shorten("welocome there") == "wlcm thr"


def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("What's TWITTER!#") == "Wht's TWTTR!#"
    assert shorten("CS50 is here") == "CS50 s hr"
