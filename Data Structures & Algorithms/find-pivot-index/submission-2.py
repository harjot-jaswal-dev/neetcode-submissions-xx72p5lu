class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)

        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
        
        return -1
        

        
       
            
