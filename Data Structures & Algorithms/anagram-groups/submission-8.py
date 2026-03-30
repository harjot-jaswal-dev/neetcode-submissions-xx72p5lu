class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapping = {}
        output = []

        for word in strs:
            sorted_wrd = sorted(word)
            sorted_word = "".join(sorted_wrd)

            if sorted_word not in mapping:
                mapping[sorted_word] = []
            mapping[sorted_word].append(word)

        for key, value in mapping.items():
            output.append(value)
        return output






