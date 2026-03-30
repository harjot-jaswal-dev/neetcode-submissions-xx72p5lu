class Solution:
    def isHappy(self, n: int) -> bool:
        
        str_num = str(n)
        seen = set()

        while True:
            result = 0
            for i in str_num:
                result += int(i) ** 2
            if result == 1:
                return True
            elif result in seen:
                return False
            seen.add(result)
            str_num = str(result)