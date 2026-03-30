class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current_num = 0

        for i in range(len(nums)):
            if nums[current_num] != nums[i]:
                current_num += 1
                nums[current_num] = nums[i]
        
        return current_num + 1
