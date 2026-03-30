class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = {}

        for i in range(len(s)):
            curr_letter = s[i]
            if curr_letter not in tracker:
                tracker[curr_letter] = 0
            tracker[curr_letter] += 1
        
        for i, char in enumerate(s):
            if tracker[char] == 1:
                return i
        return -1