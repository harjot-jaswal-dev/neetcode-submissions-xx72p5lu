class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        tracker = {}

        for i in range(len(numbers)):
            to_find = target - numbers[i]
            if to_find in tracker:
                return [tracker[to_find], i + 1]
            tracker[numbers[i]] = i + 1
        return []