class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        to_remove = 0

        for i in range(len(nums)):
            if nums[i] != nums[to_remove]:
                to_remove += 1
                nums[to_remove] = nums[i]
        return to_remove + 1