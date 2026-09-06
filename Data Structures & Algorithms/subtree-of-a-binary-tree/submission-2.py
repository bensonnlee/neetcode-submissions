# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findMatch(node, target) -> bool:
            if not node:
                return False

            if node.val == target.val:
                if check(node, target):
                    return True
            
            left = findMatch(node.left, target)
            right = findMatch(node.right, target)

            return left or right

        def check(node, target) -> bool:
            if not node and not target:
                return True
            if node and not target or not node and target:
                return False
            if node.val != target.val:
                return False
            else:
                left = check(node.left, target.left)
                right = check(node.right, target.right)
            
            return left and right

        return findMatch(root, subRoot)