class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0
        n = n

        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        
        return count
            

