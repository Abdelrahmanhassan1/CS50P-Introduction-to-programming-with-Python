from fuel import convert, gauge
import pytest


def test_one():
    assert convert('20/100') == 20
    assert convert('5/100') == 5


def test_two():
    assert gauge(convert('1/100')) == 'E'
    assert gauge(convert('100/100')) == 'F'
    assert gauge(convert('99/100')) == 'F'


def test_excepts():
    with pytest.raises(ZeroDivisionError):
        convert('10/0')

    with pytest.raises(ValueError):
        convert('moao/as')
