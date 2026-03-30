class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        total_sum = 0

        for i in range(len(nums)):
            total_sum += nums[i]
        
        expected_sum = 0

        for i in range(len(nums) + 1):
            expected_sum += i
        
        return expected_sum - total_sum