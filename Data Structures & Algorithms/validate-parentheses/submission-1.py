class Solution:
    def isValid(self, s: str) -> bool:
        
        maps = {")": "(", "]" : "[", "}":"{"}

        stack = []

        for letter in s:

            if letter in "([{":
                stack.append(letter)
            
            elif letter in maps:
                if stack:
                    if stack[-1] == maps[letter]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False