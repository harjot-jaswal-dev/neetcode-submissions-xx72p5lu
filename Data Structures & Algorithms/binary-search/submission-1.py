class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)

        while l < r:
            mid = l + (r-1) // 2
            if mid >= len(nums):
                return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r -= 1
            else:
                l += 1
        return -1