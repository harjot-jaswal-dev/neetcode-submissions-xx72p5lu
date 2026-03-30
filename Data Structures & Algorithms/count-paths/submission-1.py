class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def dp(r, c):

            if r >= m or c >= n:
                return False
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            if r == m - 1 and c == n - 1:
                return 1
            
            result = dp(r + 1, c) + dp(r, c + 1)
            memo[(r, c)] = result

            return result
        
        return dp(0, 0)