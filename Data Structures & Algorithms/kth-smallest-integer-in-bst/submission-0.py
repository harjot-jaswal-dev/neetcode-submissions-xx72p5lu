# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        sorted_arr = []

        def helper(node):

            if node is None:
                return
            
            helper(node.left)
            sorted_arr.append(node.val)
            helper(node.right)
        
        helper(root)

        if k > len(sorted_arr):
            return -1 # doesnt exist
        
        return sorted_arr[k - 1] # since k is 1 index based