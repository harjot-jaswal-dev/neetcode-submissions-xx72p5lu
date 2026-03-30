class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []

        maps = {}


        for word in strs:

            s_word = sorted(word)

            word_s = "".join(s_word)

            if word_s not in maps:

                maps[word_s] = []
            maps[word_s].append(word)
        
        

        for value in maps.values():
            result.append(value)
        
        return result


        