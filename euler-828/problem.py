import operator as o

from numbers import Integral

class Problem:
    target : int = 0
    operands : list[int] = []

    def __init__(self, target : Integral = 0, operands : list = []) -> None:
        assert isinstance(target, Integral)
        assert all([isinstance(operand, Integral) for operand in operands])
        self.target = target
        self.operands = operands