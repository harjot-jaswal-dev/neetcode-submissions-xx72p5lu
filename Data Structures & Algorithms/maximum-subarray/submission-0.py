class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = nums[0]
        current_total = nums[0]

        for i in range(1, len(nums)):
            if current_total < 0:
                current_total = nums[i]
            elif current_total >= 0:
                current_total += nums[i]
            max_total = max(max_total, current_total)
        
        return max_total

            