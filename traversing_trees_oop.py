# From Class Notebook, "Python Tree Implementation"
from __future__ import annotations
from typing import Optional


class Node:

    def __init__(self, value, left: Optional[Node] = None, right: Optional[Node] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"[{self.left}, {self.value}, {self.right}]"

    def traverse(self):
        """Traverses through the tree, returning an array of values"""
        result_values = []
        if self.left:
            result_values.extend(self.left.traverse())

        result_values.append(self.value)

        if self.right:
            result_values.extend(self.right.traverse())

        return result_values

    def find_minimum_value_node(self):
        current_node = self
        while current_node.left:
            current_node = current_node.left
        return current_node

    def has_children(self) -> bool:
        return bool(self.left or self.right)

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

    def search_for(self, target_value):
        if self.value == target_value:
            return self
        
        if self.left and self.left.value >= target_value:
            #print(f"Less than {self.value}, traversing {self.left}")
            return self.left.search_for(target_value)

        if self.right and self.right.value <= target_value:
            #print(f"Greater than {self.value}, traversing {self.right}")
            return self.right.search_for(target_value)

        raise ValueError(f"Value {target_value} is not present!")

    def delete_self(self):
        self = None

    def delete_node(self, target_value):
        target_node = self.search_for(target_value)

        if not target_node.has_children():
            target_node.delete_self()
        
        #if not target_node.left.has_children()
        

tree_root = Node(5)
values_to_insert = [3, 7, 2, 4, 6, 8]

for value in values_to_insert:
    tree_root.insert_child_value(value)

# for value in tree_root.traverse():
#     print(value)

#print("\n")
print("Looking for 8:", tree_root.search_for(8))
print("Looking for 3:", tree_root.search_for(3))
print("Looking for 7:", tree_root.search_for(7))
print("Looking for 5:", tree_root.search_for(5))
tree_root.delete_node(8)
print("Looking for 8:", tree_root.search_for(8))
#print("Looking for 99999:", tree_root.search_for(99999))