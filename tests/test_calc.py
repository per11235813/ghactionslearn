import calc
import pytest
from mymod import calc2



def test_fib():
    assert [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] == [e for e in calc.fib(10)]


def test_add():
    assert 5 == calc.add(2, 3)

def test_div():
    assert 9/3 == calc.div(9,3)

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        calc.div(1,0)

def test_fac():
    assert 120 == calc2.fac(5)

def test_fac2():
    assert 1 == calc2.fac(0)

def test_fac3():
    with pytest.raises(ValueError):
        calc2.fac(-1)