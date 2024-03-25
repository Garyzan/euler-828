import seaborn
import operator as o

from typing import Callable
from numbers import Integral
from math import floor

from node import Node
from problem import Problem
from expression import Expression

# Operator with extra properties
class op:
    def __init__(self, operator : Callable, associative : bool, risky : bool = False) -> None:
        self.fun = operator
        self.associative = associative
        self.risky = risky


# checks if l2 is sublist of l1
def sublist(l1, l2):
    for k in set(l2):
        if l2.count(k) > l1.count(k):
            return False
    return True

class Solver:
    operators : list[op] = [op(o.add, True), op(o.sub, False), op(o.mul, True), op(o.truediv, False, True)]

    def __init__(self) -> None:
        pass

    def build_expressions(self, operands : list[Integral], size : int) -> list[list[Expression]]:
        if size == 1:
            return [[Expression([k,], Node(k)) for k in operands],]
        
        sub_expressions = self.build_expressions(operands, size-1)
        sub_expressions.append([])

        for i in range(1, floor(size/2)+1):
            for (idx, i_tree) in enumerate(sub_expressions[i-1]):

                start_idx = (0, idx+1)[i == size-i]

                for j_tree in sub_expressions[(size-i)-1][start_idx:]:

                    if j_tree == i_tree:
                        continue

                    for operator in self.operators:

                        new_ops = j_tree.operands + i_tree.operands
                        if not sublist(operands, new_ops):
                            continue

                        expr = Expression(new_ops, Node(operator.fun, i_tree, j_tree))

                        if operator.risky:
                            try:
                                expr.evaluate()
                            except FloatingPointError:
                                continue
                            except ZeroDivisionError:
                                continue

                        sub_expressions[size-1].append(expr)

                        #if the operator is not associative, create new expression with swapped operands
                        if not operator.associative:
                            expr = Expression(new_ops, Node(operator.fun, j_tree, i_tree))

                            if operator.risky:
                                try:
                                    expr.evaluate()
                                except FloatingPointError:
                                    continue
                                except ZeroDivisionError:
                                    continue
                            sub_expressions[size-1].append(expr)
        return sub_expressions


    def solve(self, problem : Problem) -> tuple[Integral, list[Expression]]:

        final_expr = []
        min_score = sum(problem.operands) + 1
        expressions = self.build_expressions(problem.operands, len(problem.operands))

        for sublist in expressions:
            for expr in sublist:
                if expr.score > min_score:
                    continue

                if expr.evaluate() != problem.target:
                    continue

                if expr.score < min_score:
                    min_score = expr.score
                    final_expr = [expr]
                    
                else: final_expr.append(expr)
        
        if min_score > sum(problem.operands):
            return 0, []

        return min_score, final_expr


    def plot_all_solutions(self, problem : Problem) -> None:
        pass