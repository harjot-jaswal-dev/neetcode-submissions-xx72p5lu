class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_map = {}
        result = []

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word not in word_map:
                word_map[sorted_word] = []
            word_map[sorted_word].append(word)
        
        for key, values in word_map.items():
            result.append(values)
        return result