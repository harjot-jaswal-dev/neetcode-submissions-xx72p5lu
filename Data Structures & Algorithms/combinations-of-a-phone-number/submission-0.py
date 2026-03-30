class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz" }

        if digits == "":
            return []
        
        output = []
        curr_list = []

        def dfs(index):

            if len(curr_list) == len(digits): # we have added all possible str
                curr_str = "".join(curr_list)
                output.append(curr_str)
                return
            
            for letter in phone[digits[index]]:
                curr_list.append(letter)
                dfs(index + 1)
                curr_list.pop()
        
        dfs(0)
        return output
            




