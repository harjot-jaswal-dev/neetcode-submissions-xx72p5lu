class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        maps = {}

        
        for word in strs:

            s_word = sorted(word)

            sorted_word = "".join(s_word)
            

            if sorted_word not in maps:
                maps[sorted_word] = []
            maps[sorted_word].append(word)
        result = list(maps.values())

        return result


        