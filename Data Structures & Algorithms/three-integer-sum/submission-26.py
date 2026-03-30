class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue # next i

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    to_add = [nums[i], nums[l], nums[r]]
                    result.append(to_add)
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
        return result 