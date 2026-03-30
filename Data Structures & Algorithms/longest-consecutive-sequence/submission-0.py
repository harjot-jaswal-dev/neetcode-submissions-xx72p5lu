class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        length = 0
        if not nums:
            return 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                longest = 1

                while current + 1 in num_set:
                    current += 1
                    longest += 1
                
                length = max(length, longest)
            
        return length
