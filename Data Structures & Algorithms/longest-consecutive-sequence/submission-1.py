class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        set_nums = set(nums)
        starts = []
        sequences = []
        longest_sequence = 0

        if not nums:
            return 0

            
        for num in nums:
            if num -1 not in set_nums:
                starts.append(num)
        
        for start in starts:
            current = start
            sequence = []

            sequence.append(current)

            while current + 1 in set_nums:
                sequence.append(current + 1)
                current += 1
            
            sequences.append(sequence)
        
        for i in sequences:
            if len(i) > longest_sequence:
                longest_sequence = len(i)
        
        return longest_sequence
        