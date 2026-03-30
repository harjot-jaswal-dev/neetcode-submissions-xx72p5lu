# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        def helper(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False
            
            left_check = helper(node1.left, node2.left)
            right_check = helper(node1.right, node2.right)

            return left_check and right_check
        return helper(p, q)
        