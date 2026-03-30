class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for word in strs:
            length = len(word)
            s += str(length)+ "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        
        result = []


        i = 0
        while i < len(s):

            length = ""

            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1

            word_length = int(length)

            current_idx = i
            word = ""
            
            for j in range(word_length):

                word += s[current_idx]
                current_idx += 1
            
            result.append(word)
            i = current_idx
            
        return result

            
            
            

            

            
        
        



