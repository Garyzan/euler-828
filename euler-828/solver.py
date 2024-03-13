import seaborn
import operator as o

from problem import Problem
from expression import Expression
from typing import Union, Callable

class Solver:
    operators : list[Callable]

    def __init__(self, operators : list[Callable] = [o.add, o.sub, o.mul, o.truediv]) -> None:
        assert all([isinstance(operator, Callable) for operator in operators])
        self.operators = operators

    def solve(self, problem : Problem) -> Union[Expression, list[Expression]]:
        pass

    def plot_all_solutions(self, problem : Problem) -> None:
        pass