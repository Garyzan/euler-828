import pytest
import operator as o
from euler828 import Node, Expression

n0 = Expression([0,], Node(0))
n1 = Expression([1,], Node(1))
n2 = Expression([2,], Node(2))

def test_zerodiv_catching():
    with pytest.raises(ZeroDivisionError):
        result = Expression([0,1], Node(o.truediv, n1, n0)).evaluate()

def test_float_catching():
    with pytest.raises(FloatingPointError):
        result = Expression([1,2], Node(o.truediv, n1, n2)).evaluate()

def test_evaluate():
    result = Expression([2,1], Node(o.truediv, n2, n1)).evaluate()
    assert result == 2
