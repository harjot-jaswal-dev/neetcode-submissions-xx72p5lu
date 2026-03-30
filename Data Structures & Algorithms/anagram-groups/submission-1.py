class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for word in strs:

            new_wrd = sorted(word)
            
            full_word = "".join(new_wrd)
            
            if full_word not in hash_map:
                hash_map[full_word] = []
            hash_map[full_word].append(word)
        
        result = list(hash_map.values())
        return result