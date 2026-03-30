class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
         
        result = float("inf")
        L = 0
        curr_sum = 0

        for R in range(len(nums)):
            curr_sum += nums[R]
            while curr_sum >= target:
                result = min(result, R - L + 1)
                curr_sum -= nums[L]
                L += 1
        
        if result == float("inf"):
            return 0
        return result

