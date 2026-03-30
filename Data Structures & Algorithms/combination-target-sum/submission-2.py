class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []

        current = []


        def dfs(start):

            if sum(current) == target:
                output.append(current[:])
                return
            
            if sum(current) > target:
                return
            for i in range(start, len(nums)):

                current.append(nums[i])
                dfs(i)
                current.pop()
        
        dfs(0)
        return output

            