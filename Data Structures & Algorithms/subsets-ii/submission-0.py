class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        current = []
        nums = sorted(nums)

        def dfs(index):

            output.append(current[:])

            for i in range(index, len(nums)):
                if i > index and nums[i - 1] == nums[i]:
                    continue
                current.append(nums[i])
                dfs(i + 1)
                current.pop()
        
        dfs(0)
        return output
        


            

            
            

            
