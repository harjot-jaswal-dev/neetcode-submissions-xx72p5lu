class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         
        L = 0
        res = 0
        counter = {}
        max_char = 0
        res = 0

        for i in range(len(s)):
            letter = s[i]
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1
            max_char = max(max_char, counter[letter])
            while (i - L + 1) - max_char > k:
                counter[s[L]] -= 1
                L += 1
            res = max(res, i - L + 1)
        
        return res

