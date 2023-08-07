from numb3rs import validate

def test_max():
    assert validate("255.255.255.255") == True

def test_correct():
    assert validate("124.24.53.2") == True

def test_validinvalid():
    assert validate("76.363.13.1") == False
    
def test_outsideboundary():
    assert validate("512.512.512.512") == False

def test_neg():
    assert validate("-1.-2.4.2") == False

def test_words():
    assert validate("cat") == False
    