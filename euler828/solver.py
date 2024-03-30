#import seaborn
import operator as o

from typing import Callable
from numbers import Integral
from math import floor

from .node import Node
from .problem import Problem
from .expression import Expression

# Operator with extra properties
class op:
    def __init__(self, operator : Callable, associative : bool, risky : bool = False) -> None:
        self.fun = operator
        self.associative = associative
        self.risky = risky

OPERATORS : list[op] = [op(o.add, True), op(o.sub, False), op(o.mul, True), op(o.truediv, False, True)]

def sublist(l1 : list, l2 : list) -> bool:
    """Check if a list is a sublist of another list. Also works if the lists contain
    duplicate entries.
    
    Parameters
    ----------
    l1 : list
        List which is assumed to be the parent list.
    l2 : list
        List which is assumed to be the sublist.
    
    Returns
    -------
    bool
        Whether l2 is a sublist of l1.
        """
    for k in set(l2):
        if l2.count(k) > l1.count(k):
            return False
    return True

def _build_expressions(operands : list[Integral], size : int) -> list[list[Expression]]:
    """Recursively builds all unique expressions possible from the operands
    using multiplication, division, addition and subtraction where each operand
    can only be used once.

    Parameters
    ----------
    operands : list of integers
        Operands from which to construct the expressions.
    size : int
        Maximum size of constructed expressions.
    
    Returns
    -------
    list of list of Expressions
        All expressions with at most `size` operands, sorted ascendingly into sublists by number of operands.
        """
    if size == 1:
        return [[Expression([k,], Node(k)) for k in operands],]
    
    sub_expressions = _build_expressions(operands, size-1)
    sub_expressions.append([])

    # build all possible unique expressions by iterating through all unique
    # combinations of expressions whose lengths sum to the desired length
    for i in range(1, floor(size/2)+1):
        for (idx, i_tree) in enumerate(sub_expressions[i-1]):

            start_idx = (0, idx+1)[i == size-i]

            for j_tree in sub_expressions[(size-i)-1][start_idx:]:

                if j_tree == i_tree:
                    continue

                for operator in OPERATORS:

                    new_ops = j_tree.operands + i_tree.operands
                    if not sublist(operands, new_ops):
                        continue

                    expr = Expression(new_ops, Node(operator.fun, i_tree, j_tree))

                    # Check if the operator could cause an invalid result
                    if operator.risky:
                        try:
                            expr.evaluate()
                        except FloatingPointError:
                            continue
                        except ZeroDivisionError:
                            continue

                    sub_expressions[size-1].append(expr)

                    # If the operator is not associative, create new expression 
                    # with swapped operands
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


def solve(problem : Problem = None, target : Integral = None, operands : list[Integral] = None) -> tuple[Integral, list[Expression]]:
    """Finds the solution(s) with the lowest sum of operands 

    The function takes either a predefined Problem or a target and list of
    operands as arguments
    
    Parameters
    ----------
    problem : Problem
        The problem to solve.
    target : int
        Target number.
    operands : list of integers
        Operands from which to construct the expressions.
    
    Returns
    -------
    int
        The minimal score. `0` if the problem is not solvable.
    list of Expressions
        All expressions with the minimal score that yield the correct result.

    Raises
    ------
    ValueError
        If neither a problem nor a target number and operands are supplied
    """
    if problem is None:
        if target is None or operands is None:
            raise ValueError("You need to provide either a problem or a target number and a list of operands")
        problem = Problem(target, operands)

    final_expr = []
    min_score = sum(problem.operands) + 1
    expressions = _build_expressions(problem.operands, len(problem.operands))

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
    
    # check whether no solution has been found
    if min_score > sum(problem.operands):
        return 0, []

    return min_score, final_expr


def plot_all_solutions(problem : Problem = None, target : Integral = None, operands : list[Integral] = None) -> dict[int, int]:
    """TBD
    """
    if problem is None:
        if target is None or operands is None:
            raise ValueError("You need to provide either a problem or a target number and a list of operands")
        problem = Problem(target, operands)
    
    expressions = _build_expressions(problem.operands, len(problem.operands))
    scores : dict[int, int] = {}
    
    for sublist in expressions:
        for expr in sublist:
            if expr.evaluate() == problem.target:
                t_score = expr.score
            else:
                t_score = 0

            if t_score in scores.keys():
                scores[t_score] += 1
            else:
                scores[t_score] = 1
    
    return scores