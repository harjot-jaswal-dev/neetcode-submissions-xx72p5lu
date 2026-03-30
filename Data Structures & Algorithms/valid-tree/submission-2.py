class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        roots = list(range(n))
        size = [1] * n
        component = [n]


        def find(x):
            if roots[x] != x:
                roots[x] = find(roots[x])
            return roots[x]
        
        def union(x, y):

            p1, p2 = find(x), find(y)

            if p1 == p2:
                return False
            elif size[p1] >= size[p2]:
                roots[p2] = p1
                size[p1] += size[p2]
            else:
                roots[p1] = p2
                size[p2] += size[p1]
            
            component[0] -= 1

            return True
        
        for x, y in edges:
            if not union(x, y):
                return False
        
        if component[0] == 1:
            return True
        return False