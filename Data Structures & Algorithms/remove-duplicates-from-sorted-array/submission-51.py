class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        L, R = 0, 1
        k = 0


        while R < len(nums):
            if nums[R] != nums[L]:
                L += 1
                nums[L], nums[R] = nums[R], nums[L]
                k += 1

            R += 1
        
        
        return k + 1