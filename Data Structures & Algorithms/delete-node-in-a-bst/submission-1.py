# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # node had no children, remove set pointer to NULL
        # node had one child, remove but connect parent with the child of the node u removed
        # node has tw children
        if root is None:
            return None
            
        def min_node(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else: # found the == value
            if not root.left: # if root.left is null from here
                return root.right
            elif not root.right:
                return root.left
            else:
                min_value = min_node(root.right)
                root.val = min_value.val
                root.right = self.deleteNode(root.right, min_value.val)
        return root


            


