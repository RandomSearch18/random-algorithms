# From Class Notebook, "Python Tree Implementation"
from __future__ import annotations


class Node:

    def __init__(self, value, left: Node, right: Node) -> None:
        self.value = value
        self.left = left
        self.right = right

    def traverse(self):
        if self.left: traverse(self.left)
        print(self.value)
        if self.right: traverse(self.right)


def create_node(value):
    return {'value': value, 'left': None, 'right': None}


def insert_node(root, value):
    if root is None:
        return create_node(value)
    else:
        if value < root['value']:
            root['left'] = insert_node(root['left'], value)
        else:
            root['right'] = insert_node(root['right'], value)
        return root


def traverse(root):
    """Performs in-roder traversal, printing the outputs"""
    # Traverse left subtree
    if root['left']: traverse(root['left'])
    # Traverse root
    print(root['value'])
    # Traverse right subtree
    if root['right']: traverse(root['right'])


# Example usage:
tree_root = None
values_to_insert = [5, 3, 7, 2, 4, 6, 8]

for value in values_to_insert:
    tree_root = insert_node(tree_root, value)

print(tree_root)

traverse(tree_root)
