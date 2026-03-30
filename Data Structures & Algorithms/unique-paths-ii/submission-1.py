class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def dp(r, c):

            if r >= m or c >= n:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == m - 1 and c == n - 1:
                return 1
            
            result = dp(r + 1, c) + dp(r, c + 1)
            memo[(r, c)] = result

            return result

        return dp(0, 0) 