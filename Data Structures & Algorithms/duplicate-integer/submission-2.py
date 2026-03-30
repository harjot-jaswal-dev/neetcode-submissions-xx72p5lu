class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        maps = []

        for num in nums:
            if num in maps:
                return True
            maps.append(num)
        return False
        