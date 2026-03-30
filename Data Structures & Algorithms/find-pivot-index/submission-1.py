class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_prefix = [0] * len(nums)
        total = sum(nums)
        res = 0

        for i in range(len(nums)):
            left_prefix[i] = res
            res += nums[i]
        
        for i in range(len(nums)):
            right_sum = total - left_prefix[i] - nums[i]
            if right_sum == left_prefix[i]:
                return i
        
        return -1

        
       
            
