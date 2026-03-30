class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def helper(n):

            if n >= len(nums):
                return 0
            
            if n in memo:
                return memo[n]
            
            result = max(nums[n] + helper(n + 2), helper(n + 1))
            memo[n] = result

            return result
        
        return helper(0)