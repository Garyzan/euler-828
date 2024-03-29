from numbers import Integral

class Problem:
    """Mathematical problem in the sense of the ProjectEuler problem 828.
    
    Consists of a list of operands with which to reach a certain target number.
    """
    target : Integral = 0
    operands : list[Integral] = []

    def __init__(self, target : Integral = 0, operands : list = []) -> None:
        assert isinstance(target, Integral)
        assert all([isinstance(operand, Integral) for operand in operands])
        self.target = target
        self.operands = operands

    def __str__(self) -> str:
        return f"{self.target} : " + ", ".join([str(k) for k in self.operands])