# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        val = None

        def inorder(node):
            nonlocal counter
            nonlocal val
            
            if not node:
                return
            
            inorder(node.left)
            
            if val is not None:
                return
            counter += 1
            if counter == k:
                val = node.val
                return

            inorder(node.right)

        inorder(root)

        return val