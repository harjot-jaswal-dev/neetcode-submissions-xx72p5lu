class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        running_sum = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            running_sum[i] = prefix
            prefix *= nums[i]

        post_fix = 1

        for i in range(len(nums)-1, -1, -1):
            running_sum[i] *= post_fix
            post_fix *= nums[i]
        
        return running_sum

