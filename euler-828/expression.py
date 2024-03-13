from numbers import Integral
from typing import Callable, Union

class Expression:

    operands : list[Union[Integral, "Expression"]] = []
    operators : list[Callable] = []

    def __init__(self, operands : list[Union[Integral, "Expression"]] = [], operators : list[Callable] = []) -> None:
        assert all([type(operand) in Union[Integral, "Expression"] for operand in operands])
        assert all([type(operator) == Callable for operator in operators])
        self.operands = operands
        self.operators = operators

    def evaluate(self) -> Integral :
        def num_gen():
            i = 0
            while i < len(self.operands):
                yield self.operands[i]
                i += 1

        operands = num_gen()
        temp_result: Integral = next(operands)
        for operator in self.operators:
            temp_result = operator(temp_result, next(operands))
            if type(temp_result != Integral):
                raise FloatingPointError # We do not want to see any floating point numbers and this error unused anyways
        return temp_result
    
    def add_operation(self, operand: Union[Integral, "Expression"], operator: Callable) -> None:
        self.operands.append(operand)
        self.operators.append(operator)
