# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        base case #1:
            if tree is empty, return true
        base case #2:
            if tree only has one node, return true

        for all nodes in the tree:
            if abs(left.depth - right.depth) > 1:
                return False
            return True
        """
        is_balanced = True
        
        def dfs(node):
            nonlocal is_balanced
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            if abs(right - left) > 1:
                is_balanced = False
            
            return 1 + max(left, right)

        dfs(root)
        
        return is_balanced