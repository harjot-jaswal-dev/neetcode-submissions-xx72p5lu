class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        map1 = {}
        map2 = {}

        for letter in s:
            if letter not in map1:
                map1[letter] = 0
            map1[letter] += 1
        
        for letter in t:
            if letter not in map2:
                map2[letter] = 0
            map2[letter] += 1
        
        return map1 == map2
