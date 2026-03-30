class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        result = []

        for i in range(len(nums)):

            if i > 0:
                if nums[i] == nums[i -1]:
                    
                    continue

            l = i + 1
            r = len(nums) - 1

            while l < r and r < len(nums):

                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                
                if total == 0:
                    pair = [nums[i], nums[l], nums[r]]
                    result.append(pair)
                    
                    while l < r and nums[l] == nums[l + 1]:

                        l += 1
                    
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
                    

                    
        return result

        