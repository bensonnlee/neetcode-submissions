"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def dfs(node: 'Node') -> None:
            if not node:
                return
            
            for child in node.children:
                dfs(child)
            
            arr.append(node.val)

    
        dfs(root)
        
        return arr