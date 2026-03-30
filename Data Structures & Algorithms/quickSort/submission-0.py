# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def quickSortHelper(pairs, left, right):

            if left >= right:
                return 

            pivot = pairs[right]

            swap_point = left

            for i in range(left, right):
                if pairs[i].key < pivot.key:
                    pairs[swap_point], pairs[i] = pairs[i], pairs[swap_point]
                    swap_point += 1
            
            pairs[right], pairs[swap_point] = pairs[swap_point], pairs[right]
                
            quickSortHelper(pairs, left, swap_point - 1)
            quickSortHelper(pairs, swap_point + 1, right)
        
        quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs








