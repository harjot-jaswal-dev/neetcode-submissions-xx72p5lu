class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        current = []

        def dfs(index):

            output.append(current[:])

            # two choices append or don't append
            for i in range(index, len(nums)):
                current.append(nums[i])
                dfs(i + 1)
                current.pop()
        
        dfs(0)
        return output

            
            


            
