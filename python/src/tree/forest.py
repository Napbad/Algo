from tree import TNode
from typing import List

class Forest:
    trees: List[TNode]

    def __init__(self):
        pass

    def add_tree(self, val):
        self.trees.append(val)

    def remove_tree(self, val):
        self.trees.remove(val)

    def to_tree(self):
        pass

