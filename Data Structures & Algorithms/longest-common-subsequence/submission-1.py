class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        i = 0
        j = 0
        memo = {}

        def dp(i, j):

            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if text1[i] == text2[j]:
                result = 1 + dp(i + 1, j + 1)
                memo[(i, j)] = result
            else:
                result = max(dp(i + 1, j), dp(i, j + 1))
                memo[(i, j)] = result

            return result
        
        return dp(0, 0)

