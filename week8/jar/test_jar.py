from jar import Jar
import pytest

def test_init():
    jar = Jar(0)
    assert jar.capacity == 0
    assert jar.size == 0

    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)

    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit(-11)
    
    jar.deposit(6)
    assert jar.size == 6

def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)

    with pytest.raises(ValueError):
        jar.withdraw(8)

    with pytest.raises(ValueError):
        jar.withdraw(-1)

    jar.withdraw(4)
    assert jar.size == 3