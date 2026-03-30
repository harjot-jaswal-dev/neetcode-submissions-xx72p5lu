class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L, R = 0, len(numbers) - 1

        while L < R:
            total = numbers[L] + numbers[R]
            if total > target:
                R -= 1
                continue
            elif total < target:
                L += 1
                continue
            
            return [L + 1, R + 1]
        
        return []