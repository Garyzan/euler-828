from numbers import Integral

class Problem:
    """Mathematical problem in the sense of the ProjectEuler problem 828.
    
    Consists of a list of operands with which to reach a certain target number.
    
    Attributes
    ----------
    target : int
        Target number.
    operands : list of integers
        Operands which may be used to reach the target number.
    """
    target : Integral
    operands : list[Integral]

    def __init__(self, target : Integral, operands : list[Integral]) -> None:
        assert isinstance(target, Integral)
        assert all([isinstance(operand, Integral) for operand in operands])
        self.target = target
        self.operands = operands

    def __str__(self) -> str:
        return f"{self.target}:" + ",".join([str(k) for k in self.operands])