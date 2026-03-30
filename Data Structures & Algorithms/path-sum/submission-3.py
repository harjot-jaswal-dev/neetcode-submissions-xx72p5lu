# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None or targetSum is None:
            return False
        
        
        def dfs(node, curr_sum):

            if not node.left and not node.right:
                if curr_sum + node.val == targetSum: # at last node, add it to current sum and compare
                    return True
                else:
                    return False
            
            if node.left: # if there is a left node
                if dfs(node.left, curr_sum + node.val): # add current node value to current sum, dfs on left node
                    return True
            
            if node.right:
                if dfs(node.right, curr_sum + node.val): # add current node value to current sum, dfs on right node
                    return True
            
            # if none of these work
            return False

        if dfs(root, curr_sum = 0):
            return True
        return False




            
            
                


            


            

            


        