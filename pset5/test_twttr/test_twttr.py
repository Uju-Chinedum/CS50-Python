from twttr import shorten


def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("apple") == "ppl"


def test_upper():
    assert shorten("SMILE") == "SML"
    assert shorten("DANCE") == "DNC"


def test_number():
    assert shorten("cs50") == "cs50"
    assert shorten("f3line") == "f3ln"


def test_punctuation():
    assert shorten("12 guns") == "12 gns"
    assert shorten("__init__.py") == "__nt__.py"