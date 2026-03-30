class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = [1] * n
        running_product = 1

        for i in range(n):

            output[i] = running_product
            running_product *= nums[i]
        
        running_product = 1

        for i in range(n -1, -1, -1):

            output[i] *= running_product
            running_product *= nums[i]
        
        return output
        