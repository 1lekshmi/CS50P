from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello everyone") == 0

def test_h():
    assert value("hey") == 20
    assert value("How are you doing?") == 20

def test_other():
    assert value("good morning") == 100
    assert value("What are you up to?") == 100