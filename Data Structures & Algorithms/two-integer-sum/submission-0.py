class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for idx, num in enumerate(nums):
            to_find = target - num
            if to_find in map:
                first_idx = idx
                second_idx = map[to_find]
                return [second_idx, first_idx]
            map[num] = idx
        