import example

def test_average():
    assert example.average(10, 20) == 15

def test_add():
    assert example.add(10, 20) == 30

def test_average_neg():
    assert example.average(-10, -2) == -6
