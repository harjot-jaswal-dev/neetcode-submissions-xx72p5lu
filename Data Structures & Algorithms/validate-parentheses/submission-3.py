class Solution:
    def isValid(self, s: str) -> bool:
        
        maps = {")":"(", "]":"[", "}":"{"}

        stack = []

        for symbol in s:
            if symbol in "([{":
                stack.append(symbol)
            elif symbol in ")]}" and stack:
                top_stack = stack[-1]
                if maps[symbol] == top_stack:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        return False