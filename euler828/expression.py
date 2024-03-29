from node import Node

from numbers import Integral

class Expression:
    """Representation of a mathematical expression using a binary tree."""

    tree: Node
    operands : list[Integral]
    score : int

    def __init__(self, operands : list[Integral], tree : Node) -> None:
        self.operands = operands
        self.tree = tree
        self.score = sum(operands)

    def evaluate(self) -> Integral:
        """Evaluates the expression recursively and returns the final result as
        an integer.

        If at any point a subexpression yields a non-integral value, a
        `FloatingPointError` is raised."""
        if isinstance(self.tree.value, Integral):
            return self.tree.value

        left_val = self.tree.left.evaluate()
        right_val = self.tree.right.evaluate()

        result = self.tree.value(left_val, right_val)

        # We do not want to see any floating point numbers and this error is
        # unused anyways
        if not isinstance(result, Integral):
            raise FloatingPointError

        return result
