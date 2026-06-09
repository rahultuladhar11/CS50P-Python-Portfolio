from numb3rs import validate

def test_format():
    assert validate("123.12.31.204")
    assert not validate("45.8987.211.7")
    assert not validate("cat")
    assert not validate("178.#$%.1(8.4{2")
    assert not validate("41.204.167")
    assert not validate("213.1032.154.134")

def test_range():
    assert validate("255.255.255.255")
    assert not validate("512.512.512.512")
    assert not validate("254.255.256.257")
    assert validate("0.0.0.0")

def test_leading_zeros():
    assert not validate("123.0.33.04")
    assert not validate("0.0.0.001")
