from bank import value

def test_1():
    assert value("hello") == 0

def test_2():
    assert value("hey!") == 20

def test_3():
    assert value("123") == 100

def test_4():
    assert value("Hey!") == 20

def test_5():
    assert value("Good morning!") == 100

