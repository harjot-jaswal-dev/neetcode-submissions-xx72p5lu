class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def helper(num, memo):

            if num in memo:
                return memo[num]
            
            if num == 1 or num == 2:
                return num
            
            result = helper(num - 1, memo) + helper(num - 2, memo)

            memo[num] = result

            return result

        return helper(n, memo={})