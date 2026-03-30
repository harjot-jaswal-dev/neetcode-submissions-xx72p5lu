class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = {}

        for i in range(len(s)):
            curr_letter = s[i]
            if curr_letter not in tracker:
                tracker[curr_letter] = [i]
            else:
                tracker[curr_letter].append(i)
        
        for key, value in tracker.items():
            if len(value) == 1:
                return value[0]
        return -1