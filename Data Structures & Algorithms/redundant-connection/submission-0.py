class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        roots = []

        output = []


        for i in range(n + 1):
            roots.append(i)
        
        size = [1] * len(roots)


        def find_root(x):

            if roots[x] == x:
                return x
            return find_root(roots[x])
        
        def union(x, y):

            p1 = find_root(x)
            p2 = find_root(y)

            if p1 == p2: # same root, already added
                output.append([x, y])
            
            elif size[p1] >= size[p2]:
                roots[p2] = p1
                size[p1] += size[p2]
            else:
                roots[p1] = p2
                size[p2] += size[p1]
        
        for edge in edges:
            x, y = edge
            union(x, y)
        
        return output[-1]
        
