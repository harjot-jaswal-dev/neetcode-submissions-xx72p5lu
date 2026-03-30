class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        counter_1 = {}
        counter_2 = {}


        for letter in s:
            if letter not in counter_1:
                counter_1[letter] = 0
            counter_1[letter] += 1
        
        for letter in t:
            if letter not in counter_2:
                counter_2[letter] = 0
            counter_2[letter] += 1
        
        return counter_1 == counter_2
        