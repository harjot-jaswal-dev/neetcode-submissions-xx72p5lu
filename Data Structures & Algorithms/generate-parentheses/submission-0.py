class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def helper(current_string, opening, closing):

            if len(current_string) == n * 2:
                result.append(current_string)
                return
            
            if opening < n:
                helper(current_string + "(", opening + 1, closing)
            
            if closing < opening:
                helper(current_string + ")", opening, closing + 1)

        helper("", 0, 0)
        return result      