import pytest
from fuel import convert, gauge

def test_convert_negative_x():
    with pytest.raises(ValueError):
        convert("-1/4")

def test_convert_negative_y():
    with pytest.raises(ValueError):
        convert("2/-3")

def test_convert_x_greaterthan_y():
    with pytest.raises(ValueError):
        convert("7>4")

def test_convert_0_divsion():
    with pytest.raises(ZeroDivisionError):
        convert("6/0")

def test_convert_valid_fraction():
    assert convert("2/4") == 50
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
