# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque()

        if root:
            queue.append(root)
        
        result = []

        while len(queue) > 0:
            queue_size = len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                if i == queue_size - 1:
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return result