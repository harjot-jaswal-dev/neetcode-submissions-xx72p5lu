# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return None
        
        running_sum = [0]

        def helper(node):
            if node is None:
                return None
            
            if low <= node.val <= high:
                running_sum[0] += node.val
            
            helper(node.left)
            helper(node.right)
            
        helper(root)

        return running_sum[0] # o(n) time and space