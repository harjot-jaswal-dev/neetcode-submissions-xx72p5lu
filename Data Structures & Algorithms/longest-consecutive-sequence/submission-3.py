class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        starts = []

        set_nums = set(nums)


        for num in set_nums:
            if num - 1 not in set_nums:
                starts.append(num)

        max_sequence = 0
        for start in starts:
            curr = start
            current_sequence = 0
            while curr in set_nums:
                current_sequence += 1
                curr += 1
            if current_sequence > max_sequence:
                max_sequence = current_sequence
        return max_sequence
