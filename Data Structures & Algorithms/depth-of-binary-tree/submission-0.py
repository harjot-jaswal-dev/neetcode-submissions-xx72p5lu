# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        count = [0]
        def helper(node, level):
            if node is None:
                return 0
            count[0] = max(count[0], level)

            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 1)

        return count[0]