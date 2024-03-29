from typing import Any

class Node:
    """Node of a binary tree.

    Attributes
    ----------
    value : Any
        The value of the node.
    left : Node
        Node to the left.
    right : Node
        Node to the right.
    """
    value : Any
    left : "Node"
    right : "Node"

    def __init__(self, value : Any,  left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.left = left
        self.right = right