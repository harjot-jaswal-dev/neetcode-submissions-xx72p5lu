class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        mini_length = float("inf")
        curr_sum = 0
        L = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                mini_length = min(mini_length, R - L + 1)
                curr_sum -= nums[L]
                L += 1

            
        
        if mini_length == float("inf"):
            return 0
        
        return mini_length