import pytest
from seasons import valid_date, age_to_min, min_to_words


def test_valid_date():
    assert valid_date("asdfasf") == True
    assert valid_date("13-04-1991") == True
    assert valid_date("1996-21-05") == True
    assert valid_date("1994-10-35") == True
    assert valid_date("1991-04-13") == None
    assert valid_date("1996-05-02") == None
    assert valid_date("2002/01/01") == True

def test_age_to_min():
    assert age_to_min("1991-04-13") == 18123840.0
    assert age_to_min("1996-05-02") == 15465600.0
    assert age_to_min("2002-01-01") == 12484800.0

def test_min_to_words():
    assert min_to_words(18123840) == "Eighteen million, one hundred twenty-three thousand, eight hundred forty"
    assert min_to_words(15465600) == "Fifteen million, four hundred sixty-five thousand, six hundred"
    assert min_to_words(12484800) == "Twelve million, four hundred eighty-four thousand, eight hundred"
