class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums
        
        bucket = [0,0,0]
        
        for num in nums:
            bucket[num] += 1
        
        i = 0

        for k in range(len(bucket)):
            for j in range(bucket[k]):
                nums[i] = k
                i += 1
        return nums

        

