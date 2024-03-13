from numbers import Integral
from typing import Callable, Union

class Expression:

    operands : list[Union[Integral, "Expression"]] = []
    operators : list[Callable] = []

    def __init__(self, operands : list[Union[Integral, "Expression"]] = [], operators : list[str] = []) -> None:
        assert all([isinstance(operand, (Integral, Expression)) for operand in operands])
        assert all([isinstance(operator, Callable) for operator in operators])
        self.operands = operands
        self.operators = operators

    def evaluate(self) -> tuple[Integral, Integral]:
        score = 0

        # resolve subexpressions and calculate score
        def num_gen():
            for operand in self.operands:
                if type(operand) == Expression:
                    operand, sub_score = operand.evaluate()
                    sub_score = sub_score
                else:
                    sub_score = operand

                yield operand, sub_score

        operands = num_gen()
        result, score = next(operands)
        for operator in self.operators:
            operand, sub_score = next(operands)
            result = operator(result, operand)
            score += sub_score
            if not isinstance(result, Integral):
                raise FloatingPointError # We do not want to see any floating point numbers and this error is unused anyways
        return result, score
    
    def add_operation(self, operand: Union[Integral, "Expression"], operator: Callable) -> None:
        self.operands.append(operand)
        self.operators.append(operator)
