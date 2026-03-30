# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def helper(node, current_path):
            if node is None:
                return 0
            
            current_path = current_path * 10 + node.val

            if node.left is None and node.right is None:
                return current_path
            
            left_check = helper(node.left, current_path)
            right_check = helper(node.right, current_path)
            return left_check + right_check
        return helper(root, current_path= 0) # o(n) time and space