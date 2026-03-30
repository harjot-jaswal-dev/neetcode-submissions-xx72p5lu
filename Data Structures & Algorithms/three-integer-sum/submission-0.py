class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        target = 0
        results = []
        pairs = []
        nums = sorted(nums)

        for i in range(len(nums)):
            L = i + 1
            R = len(nums) - 1

            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue

            while L < R and R < len(nums):
                
                total = nums[i] + nums[L] + nums[R]
                
                if total > target:
                    R -= 1
                elif total < target:
                    L += 1
                
                if total == target:
                    pairs = [nums[i], nums[L], nums[R]]
                    results.append(pairs)

                    
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while R > L and nums[R] == nums[R - 1]:
                        R -= 1
                    R -= 1
                    L += 1
        
        return results