# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        node's left subtree's max value must be less than node

        node's right subtree's min values must be more than node
        """
        def helper(node):
            if not node:
                return (True, float('inf'), float('-inf'))
            
            left = helper(node.left)
            right = helper(node.right)

            is_valid = left[2] < node.val < right[1]
            return (is_valid and left[0] and right[0], min(left[1], node.val), max(right[2], node.val))

        return helper(root)[0]