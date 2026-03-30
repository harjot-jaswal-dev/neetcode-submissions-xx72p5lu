class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)

        tracker = {}

        for num in nums:
            if num not in tracker:
                tracker[num] = 0
            tracker[num] += 1
        
        for key, value in tracker.items():
            if value > (n // 2):
                return key