class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = ""
        new_number = []

        for num in digits:
            number += str(num)
        
        int_number = int(number)

        int_number = int_number + 1

        str_number = str(int_number)

        for i in range(len(str_number)):
            new_number.append(int(str_number[i]))
        
        return new_number
