# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif subRoot is None:
            return True
        elif root is None:
            return False
        
        def isIdentical(node, subNode):
            if node is None and subNode is None:
                return True
            elif node and subNode is None:
                return False
            elif subNode and node is None:
                return False

            if node.val != subNode.val:
                return False
            
            return isIdentical(node.left, subNode.left) and isIdentical(node.right, subNode.right)
        
        if isIdentical(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)