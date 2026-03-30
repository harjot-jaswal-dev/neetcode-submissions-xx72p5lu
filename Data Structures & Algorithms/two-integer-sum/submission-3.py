class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tracker = {}

        for i in range(len(nums)):
            find = target - nums[i]
            if find in tracker:
                return [tracker[find], i]
            tracker[nums[i]] = i  