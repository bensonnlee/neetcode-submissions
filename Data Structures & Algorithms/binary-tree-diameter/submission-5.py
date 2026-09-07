# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # given a node, return 1 + max(left, right)
        def helper(node):
            nonlocal ans
            # base case:
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            # something here is missing
            ans = max(ans, left + right)

            return 1 + max(left, right)
        
        helper(root)

        return ans