class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        seen = set()

        curr_longest = 0
        L = 0

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                curr_longest -= 1
                L += 1

            seen.add(s[R])
            curr_longest += 1
            res = max(res, curr_longest)
        
        return res
            