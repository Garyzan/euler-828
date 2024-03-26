from typing import Any

# Node of a binary tree
class Node:
    value : Any
    left : "Node"
    right : "Node"

    def __init__(self, value : Any,  left: "Node" = None, right: "Node" = None) -> None:
        self.value = value
        self.left = left
        self.right = right