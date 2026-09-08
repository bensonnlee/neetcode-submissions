# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')

        def helper(node):
            nonlocal max_path

            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            max_path = max(max_path, node.val + max(0, left) + max(0, right))

            return node.val + max(left, right, 0)

        helper(root)

        return max_path