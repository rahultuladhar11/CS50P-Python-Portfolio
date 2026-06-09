from twttr import shorten

def test_1():
    assert shorten("cat") == "ct"

def test_2():
    assert shorten("123") == "123"

def test_3():
    assert shorten("CS50P") == "CS50P"

def test_4():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_5():
    assert shorten("Dog") == "Dg"

def test_6():
    assert shorten("Omen") == "mn"

