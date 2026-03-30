class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        longest_sequence = 0

        starts = []

        for num in nums:
            if num - 1 not in nums:
                starts.append(num)
        
        for start in starts:
            curr = start
            sequence_length = 0
            while curr in nums:
                sequence_length += 1
                curr += 1
            longest_sequence = max(longest_sequence, sequence_length)
        
        return longest_sequence
