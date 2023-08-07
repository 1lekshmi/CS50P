from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/12") == 0
    
def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(26) == "26%"