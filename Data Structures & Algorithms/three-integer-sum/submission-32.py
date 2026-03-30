class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        nums = sorted(nums)

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 # how does this skip all duplicates lets say i was -1, i + 1 is also -1, and if we do i + 1 again its also -1, like there are 4 consective -1 at i?
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    
        return result