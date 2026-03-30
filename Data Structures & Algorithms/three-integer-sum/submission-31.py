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
                    if nums[l] == nums[l - 1]:
                        l += 1
                    if nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    
        return result