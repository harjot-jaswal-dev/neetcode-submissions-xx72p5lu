class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        if not isConnected:
            return len(isConnected) # no connections so one whole city
        
        i = len(isConnected)
        j = len(isConnected[0])
        
        visited = set()
        count = 0
        n = i


        def dfs(node): 

            if node in visited:
                return

            visited.add(node)

            for i in range(n):
                if isConnected[node][i] == 1:
                    dfs(i)
        
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count