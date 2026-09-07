# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        bfs but only keep the first right element in each row
        """
        queue = deque()
        ans = []

        if not root:
            return ans

        queue.append(root)

        # queue =   [1]

        while queue:
            ans.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


        return ans