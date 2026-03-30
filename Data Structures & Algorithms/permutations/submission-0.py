class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        current = []

        def dfs():

            if len(current) == len(nums):
                output.append(current[:])
                return
            
            for num in nums:
                if num not in current:
                    current.append(num)
                    dfs()
                    current.pop()

            
        dfs() # how does not having a parameter in dfs work, I have always seen a parameter in dfs
        return output
            


        

            