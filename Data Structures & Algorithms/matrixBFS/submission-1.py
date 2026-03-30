from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        if not grid or grid[0][0] != 0:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        length = 0
        visited = set()

        queue = deque([(0, 0)])
        visited.add((0, 0))


        while queue:

            for i in range(len(queue)):

                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:

                    if min(r + dr, c + dc) < 0 or dr + r >= rows or dc + c >= cols or (r + dr, c + dc) in visited or grid[r + dr][c + dc] != 0:
                        continue # next direction
                    
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1
        
        return -1