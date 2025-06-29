from um import count


def test_case():
    assert count("Um, um, UM,") == 3

def test_substring():
    assert count("Yummy, mummy, mum") == 0

def test_string():
    assert count("I think I um, I might um... never mind.") == 2
