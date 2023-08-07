from um import count

def test_um():
    assert count("hello, um, world") == 1
    assert count("hello, um, yummy") == 1

def test_um_cap():
    assert count("hello. UM, world") == 1
    assert count("hello. UM, yummy") == 1

def test_wordswithum():
    assert count("yummy") == 0
    assert count("mum") == 0
    