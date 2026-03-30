class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        string_s = {}
        string_t = {}

        for letter in s:
            if letter not in string_s:
                string_s[letter] = 0
            string_s[letter] += 1
        
        for letter in t:
            if letter not in string_t:
                string_t[letter] = 0
            string_t[letter] += 1
        
        return string_s == string_t