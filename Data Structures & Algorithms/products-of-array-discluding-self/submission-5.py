class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prefix = [0] * len(nums)
        right_prefix = [0] * len(nums)
        total = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            left_prefix[i] = total
            total *= nums[i]
        
        total = 1
        for i in range(len(nums) -1, -1, -1):
            right_prefix[i] = total
            total *= nums[i]
        
        for i in range(len(nums)):
            res[i] = left_prefix[i] * right_prefix[i]
        
        return res

