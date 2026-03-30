class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        to_move = 0

        for i in range(len(nums)):
            if nums[i] != nums[to_move]:
                to_move += 1
                nums[to_move] = nums[i]
        
        return to_move + 1