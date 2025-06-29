from twttr import shorten

def test_shorten_upper():
    assert shorten("ACRYMONY") == "CRYMNY"

def test_shorten_lower():
    assert shorten("acrymony") == "crymny"

