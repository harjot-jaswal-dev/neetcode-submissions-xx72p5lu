class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        result = [1] * n
        
        running = 1

        for i in range(n -1, -1, -1):
            result[i] = running
            running *= nums[i]

        running = 1

        for i in range(n):
            result[i] *= running
            running *= nums[i]


        return result
            
