class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        tracker = {}

        for num in nums:
            if num in tracker:
                return True
            elif num not in tracker:
                tracker[num] = 0
            tracker[num] += 1
        return False
