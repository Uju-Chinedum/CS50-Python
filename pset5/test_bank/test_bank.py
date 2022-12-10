from bank import value


def test_zero():
    assert value("hello") == 0
    assert value("HELLO, WORLD") == 0

def test_twenty():
    assert value("hi") == 20
    assert value("HEY") == 20

def test_hundred():
    assert value("good day") == 100
    assert value("BONJOUR") == 100

def test_others():
    assert value("1") == 100
    assert value("'hello'") == 100