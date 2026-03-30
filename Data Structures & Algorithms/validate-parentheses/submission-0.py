class Solution:
    def isValid(self, s: str) -> bool:

        matches = {")": "(", "}": "{", "]": "["}

        my_stack = []

        for i in s:

            if i in "([{":
                my_stack.append(i)

            if i in matches:
                match_item = matches[i]
                if not my_stack:
                    return False
                if my_stack[-1] == match_item:
                    my_stack.pop()
                else:
                    return False
        if not my_stack:
            return True
        else:
            return False
        