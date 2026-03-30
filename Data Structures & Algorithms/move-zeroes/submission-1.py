class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for i in range(len(nums)):
            if nums[i] != 0 and nums[l] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[l] != 0:
                l += 1
        return nums