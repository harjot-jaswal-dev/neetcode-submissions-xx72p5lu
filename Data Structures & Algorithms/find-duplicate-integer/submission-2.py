class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        tracker = set()

        for i in range(len(nums)):
            if nums[i] in tracker:
                return nums[i]
            
            tracker.add(nums[i])
        
