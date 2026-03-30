"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None


        mapping = {}
        queue = deque()
        queue.append(node)
        cloned = Node(node.val)
        mapping[node] = cloned


        while queue:

            curr_node = queue.popleft()

            curr_clone = mapping[curr_node]

            for neighbor in curr_node.neighbors:
                if neighbor not in mapping:
                    cloned_neighbor = Node(neighbor.val)
                    mapping[neighbor] = cloned_neighbor
                    queue.append(neighbor)
                curr_clone.neighbors.append(mapping[neighbor])
                
        
        return mapping[node]
