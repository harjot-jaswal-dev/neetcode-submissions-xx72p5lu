class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        results = []

        def helper(index, subset):

            if sum(subset) == target:
                return results.append(subset[:]) # if any point our subset == target, append
            
            if sum(subset) > target:
                return
            
            if index >= len(nums):
                return
            
            subset.append(nums[index])
            helper(index, subset) # same number as many times
            subset.pop() # pop it
            helper(index + 1, subset) # next number

        helper(0, [])

        return results

         
            



                


