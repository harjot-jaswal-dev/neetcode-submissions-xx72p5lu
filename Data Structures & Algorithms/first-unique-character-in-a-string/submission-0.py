class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = {}
        # key is letter, value is list if indexex
        for i in range(len(s)):
            if s[i] not in tracker:
                tracker[s[i]] = []
            tracker[s[i]].append(i)
        
        for key, values in tracker.items():
            if len(tracker[key]) < 2:
                result = tracker[key]
                return result[0]
        return -1