import pytest
from jar import Jar

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_over_deposit():
    jar = Jar(5)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    assert str(jar) == "🍪🍪"

def test_over_withdraw():
    jar = Jar()
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_negative_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_negative_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)
