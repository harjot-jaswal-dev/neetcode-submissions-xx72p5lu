class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_tracker = {0: 1}
        total = 0
        res = 0

        for i in range(len(nums)):
            total += nums[i]
            to_find = total - k
            if to_find in prefix_tracker:
                res += prefix_tracker[to_find]
            if total not in prefix_tracker:
                prefix_tracker[total] = 0
            prefix_tracker[total] += 1
        
        return res


        
        


            


            
                