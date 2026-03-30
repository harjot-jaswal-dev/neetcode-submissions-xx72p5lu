class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        if not isConnected:
            return len(isConnected) # no connections so one whole city
        
        i = len(isConnected)
        j = len(isConnected[0])

        graph = {}

        for a in range(i):
            graph[a] = []
        
        for x in range(i):
            for y in range(j):
                if isConnected[x][y] == 1:
                    graph[x].append(y)
        
        visited = set()
        count = 0

        def dfs(node): 

            if node in visited:
                return

            visited.add(node)

            for child in graph[node]:
                dfs(child)
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count