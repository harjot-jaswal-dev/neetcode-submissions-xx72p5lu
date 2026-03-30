class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        maps = {}

        for idx, num in enumerate(nums):

            to_find = target - num

            if to_find in maps:
                return [maps[to_find], idx]
            if to_find not in maps:
                maps[num] = idx
            
        