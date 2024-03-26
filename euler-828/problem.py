from numbers import Integral

class Problem:
    target : Integral = 0
    operands : list[Integral] = []

    def __init__(self, target : Integral = 0, operands : list = []) -> None:
        assert isinstance(target, Integral)
        assert all([isinstance(operand, Integral) for operand in operands])
        self.target = target
        self.operands = operands

    def __str__(self) -> str:
        return f"{self.target} : " + ", ".join([str(k) for k in self.operands])