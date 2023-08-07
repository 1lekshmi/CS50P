import pytest
from working import convert

def test_valid():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_validPMtoAM():
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

def test_midnighttomidday():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_middaytomidnight():
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_invalidto():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 PM - 5 AM")

def test_invalidmins():
    with pytest.raises(ValueError):
        convert("9:70 AM to 5:40 PM")
    with pytest.raises(ValueError):
        convert("9:70 PM to 5:40 AM")
