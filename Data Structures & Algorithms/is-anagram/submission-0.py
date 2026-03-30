class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_1 = {}

        for letter in s:
            if letter in map_1:
                map_1[letter] +=1
            else:
                map_1[letter] = 1
        
        map_2 = {}

        for letter in t:
            if letter in map_2:
                map_2[letter] +=1
            else:
                map_2[letter] = 1
        
        return map_1 == map_2
        
        