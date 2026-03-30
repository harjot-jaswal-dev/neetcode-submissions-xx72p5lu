class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

            sig = "".join(sorted(word))

            if sig not in groups:
                groups[sig] = []
            groups[sig].append(word)
        
        return list(groups.values())

        