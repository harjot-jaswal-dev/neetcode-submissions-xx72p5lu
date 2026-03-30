"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: # no node/list so return empty list
            return None
        
        mapping = {}

        def clone(node, mapping):

            if not node:
                return None
            
            if node in mapping:
                return mapping[node]

            cloned = Node(node.val)
            mapping[node] = cloned 
            

            for neighbor in node.neighbors:
                result = clone(neighbor, mapping) # so go all the way down
                cloned.neighbors.append(result) # add the neighbors going back up

            return cloned
        return clone(node, mapping)
