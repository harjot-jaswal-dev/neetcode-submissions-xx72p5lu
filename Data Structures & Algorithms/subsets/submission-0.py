class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = []

        def helper(index, subset):

            if index >= len(nums):
                results.append(subset[:])
                return
            
            subset.append(nums[index])
            helper(index + 1, subset)
            subset.pop()
            helper(index + 1, subset)
        
        helper(0, [])

        return results
            