from working import convert
import pytest


def test_valid_time():
    assert convert("9 AM to 5 PM") == "09:00 AM to 17:00 PM"
    assert convert("9:00 AM to 5:00 PM") == "09:00 AM to 17:00 PM"
    assert convert("10 AM to 8:50 PM") == "10:00 AM to 20:50 PM"

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")



