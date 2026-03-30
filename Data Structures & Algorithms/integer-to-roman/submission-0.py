class Solution:
    def intToRoman(self, num: int) -> str:
        

        values = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        res = ""
        for val, letter in values:
            
            if num // val != 0:
                count = num // val
                to_add = letter * count
                res += to_add
                num = num % val
        
        return res


