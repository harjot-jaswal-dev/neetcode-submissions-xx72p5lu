class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        starts = []
        max_sequence = 0

        for num in nums:
            if num - 1 not in nums:
                starts.append(num)
        
        for start in starts:
            current_sequence = 0
            num = start
            while num in nums:
                current_sequence += 1
                num += 1
            max_sequence = max(max_sequence, current_sequence)
        return max_sequence

