class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largest_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum >= 0:
                current_sum += nums[i]
            elif current_sum < 0:
                current_sum = nums[i]
            largest_sum = max(largest_sum, current_sum)
        return largest_sum