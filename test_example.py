# test_example.py

from example import add, subtract

def test_add():
    assert add(3, 2) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 2) == 0
    assert subtract(0, 1) == -1
