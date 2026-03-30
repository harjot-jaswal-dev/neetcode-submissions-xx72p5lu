class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for word in strs:
            length = len(word)
            s += str(length) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:

        result = []

        i = 0

        while i < len(s):

            j = i

            while s[j] != "#":
                j += 1
            
            length_s = s[i:j]
            length = int(length_s)

            start = j + 1
            end = j + 1 + length

            word = s[start:end]

            result.append(word)

            i = end
        return result
