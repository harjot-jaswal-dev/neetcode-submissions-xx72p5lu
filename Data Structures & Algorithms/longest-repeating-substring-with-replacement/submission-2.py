class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        counter = {}
        L = 0
        max_frequency = 0
        res = 0


        for R in range(len(s)):
            letter = s[R]
            if letter not in counter:
                counter[letter] = 0
            counter[letter] += 1
            max_frequency = max(max_frequency, counter[letter])
            while (R - L + 1) - max_frequency > k:
                counter[s[L]] -= 1
                L += 1
            # at this point window is valid
            res = max(res, R - L + 1)

        return res

        
