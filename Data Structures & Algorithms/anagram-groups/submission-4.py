class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        maps = {}

        for word in strs:

            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word not in maps:
                maps[sorted_word] = []
            maps[sorted_word].append(word)

        for value in maps.values():
            result.append(value)
        
        return result



