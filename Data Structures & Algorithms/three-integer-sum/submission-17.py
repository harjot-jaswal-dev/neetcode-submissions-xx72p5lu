class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums = sorted(nums)

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            if i > 0:
                if nums[i] == nums[i - 1]:
                    i += 1
                    continue
            
            while l < r:
                total = nums[i] + nums[r] + nums[l]

                if total > 0:
                    r -= 1
                    continue
                if total < 0:
                    l += 1
                    continue
                if total == 0:
                    pair = [nums[i], nums[l], nums[r]]
                    result.append(pair)
                
                while l < r and nums[l] == nums[l + 1]:
                    l +=1
                while r > l and nums[r] == nums[r - 1]:
                     r-= 1 
                l += 1
                r -= 1
        return result
        