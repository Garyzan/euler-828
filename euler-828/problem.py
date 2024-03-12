import operator as o

from numbers import Integral
from typing import Callable

class Problem:
    target : int = 0
    operands : list[int] = []
    operators: list[Callable]

    def __init__(self, target : Integral = 0,
                 operands : list = [],
                 operators : list[Callable] = [o.add, o.mul, o.truediv, o.sub]) -> None:
        assert type(target) == Integral
        assert all([type(operand) == Integral for operand in operands])
        assert all([type(operator) == Callable for operator in operators])
        self.target = target
        self.operands = operands
        self.operators = operators