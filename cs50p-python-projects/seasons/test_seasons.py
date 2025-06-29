from seasons import convert_to_minutes, convert_to_words
import pytest


def test_convert_dob():
    assert convert_to_minutes("2024-05-27") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_minutes("2023-05-27") == "One million, fifty-two thousand, six hundred forty minutes"

def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_words(1052640) == "One million, fifty-two thousand, six hundred forty minutes"

def test_format():
    with pytest.raises(SystemExit):
            convert_to_minutes("20-05-2000")

