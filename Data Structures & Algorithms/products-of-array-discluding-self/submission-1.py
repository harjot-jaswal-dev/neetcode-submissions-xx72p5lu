class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        running_product = 1
        n = len(nums)

        result = [1] * n
        

        for i in range(n):

            result[i] = running_product
            running_product *= nums[i]
        running_product = 1
        for i in range(n -1, -1, -1):

            result[i] *= running_product
            running_product *= nums[i]
        return result
        
        

            
        