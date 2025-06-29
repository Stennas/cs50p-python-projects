from plates import is_valid

def test_first_two_char():
    assert is_valid("cs50") == True
    assert is_valid("c50s") == False

def test_length():
   assert is_valid("c") == False
   assert is_valid("cs") == True
   assert is_valid("cs5") == True
   assert is_valid("cs50") == True
   assert is_valid("cs501") == True
   assert is_valid("cs5012") == True
   assert is_valid("cs10000") == False

def test_only_alnum():
    assert is_valid("CS.PY") == False  # Invalid character
    assert is_valid("CS50") == True
    assert is_valid("CS PY") == False

def test_zero_position():
    assert is_valid("CS05") == False  # Number can't start with 0
    assert is_valid("CS50") == True

def test_numbers_middle():
    assert is_valid("CS5P0") == False  # Numbers must be at end
