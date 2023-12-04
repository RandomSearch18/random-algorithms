# From Class Notebook, "Python Tree Implementation"
from __future__ import annotations
from typing import Optional


class Node:

    def __init__(self, value, left: Optional[Node] = None, right: Optional[Node] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.value}"

    def traverse(self):
        """Traverses through the tree, returning an array of values"""
        result_values = []
        if self.left:
            result_values.extend(self.left.traverse())

        result_values.append(self.value)

        if self.right:
            result_values.extend(self.right.traverse())

        return result_values

    def insert_child_value(self, value):
        if value < self.value:
            if not self.left:
                self.left = Node(value)
                return
            self.left.insert_child_value(value)
        else:
            if not self.right:
                self.right = Node(value)
                return
            self.right.insert_child_value(value)

tree_root = Node(5)
values_to_insert = [3, 7, 2, 4, 6, 8]

for value in values_to_insert:
    tree_root.insert_child_value(value)

for value in tree_root.traverse():
    print(value)