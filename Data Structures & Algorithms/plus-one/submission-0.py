class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_str = ""
        result = []

        for num in digits:
            number_str += str(num)
        
        number = int(number_str)
        number = number + 1
        back_str = str(number)

        for i in range(len(back_str)):
            result.append(int(back_str[i]))
        return result