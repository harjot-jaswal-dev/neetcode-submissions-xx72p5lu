class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 1 and edges is None:
            return True
        
        if edges is None:
            return False
        
        graph = {}

        for i in range(n):
            graph[i] = []

        for edge in edges:
            num1, num2 = edge
            graph[num1].append(num2)
            graph[num2].append(num1)
        
        visited = set()
        
        def dfs(current, parent):

            if current in visited:
                return False
            
            visited.add(current)

            for node in graph[current]:
                if node == parent:
                    continue
                if not dfs(node, current):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n


