from numb3rs import validate

def test_str():
    assert validate("cat") == False

def test_number_limit():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.0") == True
    assert validate("256.1.1.1") == False
