class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        maps = {}
        result = []

        for word in strs:
            sorted_word = sorted(word)

            joined_word = "".join(sorted_word)

            if joined_word not in maps:
                maps[joined_word] = []
            maps[joined_word].append(word)
        
        for key, value in maps.items():
            result.append(value)
        
        return result
            
