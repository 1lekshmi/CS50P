from seasons import sing, days_to_mins
from datetime import date

def test_sing():
    assert sing(date.fromisoformat("2020-12-01")) == "One million, four hundred sixty-three thousand forty minutes"
    assert sing(date.fromisoformat("2023-09-12")) == "One thousand, four hundred forty minutes"
    assert sing(date.fromisoformat("2022-09-13")) == "Five hundred twenty-five thousand, six hundred minutes"
    assert sing(date.fromisoformat("2021-09-13")) == "One million, fifty-one thousand, two hundred minutes"

def test_days_to_mins():
    assert days_to_mins(date.fromisoformat("2020-12-01"),date.today()) == 1463040
    assert days_to_mins(date.fromisoformat("2023-09-12"),date.today()) == 1440
    assert days_to_mins(date.fromisoformat("2022-09-13"),date.today()) == 525600
    assert days_to_mins(date.fromisoformat("2021-09-13"),date.today()) == 1051200
