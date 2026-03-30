class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        bucket = []
        starts = []

        for i in range(len(nums)):
            bucket.append([])
        
        for num in sorted_nums:
            if num - 1 not in nums:
                starts.append(num)
        longest_sequence = 0

        for start in starts:
            current_num = start
            current_sequence = 0
            while current_num in sorted_nums:
                current_sequence += 1
                current_num += 1
            if current_sequence > longest_sequence:
                longest_sequence = current_sequence
        return longest_sequence
