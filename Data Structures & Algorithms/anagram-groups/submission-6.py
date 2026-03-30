class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        maps = {}
        result = []

        for word in strs:
            #print(word)
            new_word = sorted(word)
            new_word = "".join(new_word)
            
            if new_word not in maps:
                maps[new_word] = []
            maps[new_word].append(word)
        
        for values in maps.values():
            result.append(values)
        
        return result
        
        