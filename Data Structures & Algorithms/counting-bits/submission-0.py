class Solution:
    def countBits(self, n: int) -> List[int]:

        count = []

        for i in range(n + 1):
            count.append(0)
        
        
        for curr_num in range(n + 1):
            i = curr_num
            while i > 0:
                if i & 1 == 1:
                    count[curr_num] += 1
                i = i >> 1
        
        return count

