from numbers import Integral

class Problem:
    target : int = 0
    operands : list[int] = []

    def __init__(self, target : Integral = 0, operands : list = []) -> None:
        assert type(target) == Integral
        assert all([type(operand) == Integral for operand in operands])
        self.target = target
        self.operands = operands