from um import count

def test_pneumatic():
    assert count("pneumatic") == 0

def test_umbilical():
    assert count("umbilical") == 0

def test_potassium():
    assert count("potassium") == 0

def test_hello():
    assert count("Hello, um, world!") == 1
    assert count("Um, this is the end! um....bye!") == 2
    assert count("How about we, um ummm, go to, umm um McDonalds!?") == 2
