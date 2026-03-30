class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #nums = set(nums)

        longest = 0
        starts = []

        for num in nums:
            if num - 1 not in nums:
                starts.append(num)
        

        for start in starts:
            current = 0
            num = start
            while num in nums:
                current += 1
                num += 1
                longest = max(longest, current)
        
        return longest


