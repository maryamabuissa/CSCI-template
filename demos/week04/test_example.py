import example
from pytest import approx 

def test_add_pos():
    assert(example.add(0.1, 0.2) == approx(0.3))

def test_add_pos_neg():
    assert(example.add(-3, 3) == 0)

def test_add_neg():
    assert(example.add(-3, -3) == -6)

def test_average():
    assert(example.average(1, 3) == 2.0)
    assert(example.average(1, 2) == 1.5)
    assert(example.average(1, -1) == 0.0)
