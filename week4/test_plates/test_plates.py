from plates.plates import is_valid

def test_length():
    assert is_valid("2") == False
    assert is_valid("HL") == True
    assert is_valid("LSK152") == True
    assert is_valid("AAA22345") == False
    assert is_valid("H") == False

def test_start():
    assert is_valid("LS1998") == True
    assert is_valid("12LS15") == False
    assert is_valid("LS") == True
    assert is_valid("15") == False

def test_num():
    assert is_valid("134KLM") == False
    assert is_valid("AAA22A") == False
    assert is_valid("BBB333") == True
    assert is_valid("LSK012") == False

def test_punc():
    assert is_valid("LSK!15") == False
    assert is_valid(".13LSK") == False
    assert is_valid("LS 152") == False
