class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_res = 0

        for num in nums:
            current_len = 0
            if num - 1 not in num_set:
                current_len += 1
                curr = num
                while curr + 1 in num_set:
                    current_len += 1
                    curr += 1
                max_res = max(max_res, current_len)
        
        return max_res
