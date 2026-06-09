import pytest
from working import convert

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("9: PM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:30 AM to 5: AM")
    with pytest.raises(ValueError):
        convert("12 PM - 5:30 AM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("123456789")

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("8:45AM to 7:15PM")
    with pytest.raises(ValueError):
        convert("9:00 pm to 5:30 pm")
    with pytest.raises(ValueError):
        convert("14 AM to 12:13 PM")
    with pytest.raises(ValueError):
        convert("12:90 PM to 5:87 AM")
    with pytest.raises(ValueError):
        convert("12:16 PM to 17:45 PM")

def test_valid():
    assert convert("5:00 PM to 3:00 AM") == "17:00 to 03:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:28 PM to 12:48 AM") == "12:28 to 00:48"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("8 AM to 4 PM") == "08:00 to 16:00"

