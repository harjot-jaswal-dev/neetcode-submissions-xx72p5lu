import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        copy_stones = []

        for x in stones:
            copy_stones.append(-x)
        
        heapq.heapify(copy_stones)
        while len(copy_stones) > 1:
            y = heapq.heappop(copy_stones)
            x = heapq.heappop(copy_stones)
            result = -(y) - (-(x))
            if result > 0:
                heapq.heappush(copy_stones, -(result))
        
        if len(copy_stones) == 1:
            return -(copy_stones[0])
        return 0