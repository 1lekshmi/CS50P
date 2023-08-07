from twttr import shorten

def test_vowels():
    assert shorten("hello") == "hll"

def test_const():
    assert shorten("cs") == "cs"

def test_vowelsup():
    assert shorten("Indigo") == "ndg"

def test_constup():
    assert shorten("Rhythms") == "Rhythms"

def test_nums():
    assert shorten("CS50") == "CS50"

def test_punc():
    assert shorten("What's your name?") == "Wht's yr nm?"
