"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}

        def clone(n):
            if n in copies:
                return copies[n]
            else:
                copy = Node(n.val)
                copies[n] = copy

                for nb in n.neighbors:
                    copy.neighbors.append(clone(nb))

            return copy

        if not node:
            return None

        return clone(node)