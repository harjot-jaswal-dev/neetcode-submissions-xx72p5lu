class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        memo = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        def dfs(r, c):

            if r >= rows or c >= cols:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == rows - 1 and c == cols - 1:
                return 1
                
            if (r, c) in memo:
                return memo[(r, c)]
            
            result = dfs(r + 1, c) + dfs(r, c + 1)
            memo[(r, c)] = result

            return result
        
        return dfs(0, 0)