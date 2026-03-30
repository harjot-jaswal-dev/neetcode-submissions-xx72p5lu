# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        if len(pairs) <= 1:
            return pairs
        
        middle = len(pairs) // 2
        left_side = pairs[:middle]
        right_side = pairs[middle:]

        sorted_left = self.mergeSort(left_side)
        sorted_right = self.mergeSort(right_side)

        def merge(sorted_left, sorted_right):

            result = []
            left_pointer = 0
            right_pointer = 0

            while left_pointer < len(sorted_left) and right_pointer < len(sorted_right):
                if sorted_left[left_pointer].key <= sorted_right[right_pointer].key:
                    result.append(sorted_left[left_pointer])
                    left_pointer += 1
                else:
                    result.append(sorted_right[right_pointer])
                    right_pointer += 1
            
            # once loop is done add remaining
            result += sorted_left[left_pointer:]
            result += sorted_right[right_pointer:]
            return result

        return merge(sorted_left, sorted_right)