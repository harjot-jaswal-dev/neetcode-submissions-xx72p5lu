class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_prefix = [0] * len(nums)
        right_prefix = [0] * len(nums)
        total = 0

        for i in range(len(nums)):
            left_prefix[i] = total
            total += nums[i]
        
        total = 0

        for i in range(len(nums) -1, -1, -1):
            right_prefix[i] = total
            total += nums[i]
        
        for i in range(len(nums)):
            if left_prefix[i] == right_prefix[i]:
                return i
        
        return -1
            
