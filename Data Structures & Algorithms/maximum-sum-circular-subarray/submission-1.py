class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        # get regular max subarray
        # get minimum subarray
        # get circular subarray which is total sum of nums - minimum subarray
        # get max of these

        reg_max = nums[0]
        curr_reg = 0

        sub_mini = nums[0]
        curr_mini = 0

        total = 0

# reg max is -1
# sub mini is 

        for num in nums:
            curr_reg = max(curr_reg, 0)
            curr_reg += num
            reg_max = max(curr_reg, reg_max)
        
        for num in nums:
            curr_mini = min(curr_mini, 0)
            curr_mini += num
            sub_mini = min(sub_mini, curr_mini)
            total += num
        
        if total - sub_mini == 0 and reg_max < 0:
            return reg_max


        return max(reg_max, total - sub_mini)
        


        