class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        maps = {}

        for i in range(len(nums)):
            to_find = target - nums[i]
            if to_find in maps:
                return [maps[to_find], i]
            else:
                maps[nums[i]] = i
