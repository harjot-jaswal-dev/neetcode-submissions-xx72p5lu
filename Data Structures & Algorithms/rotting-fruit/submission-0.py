from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        fresh_fruit = 0
        rotten = 0
        minutes = 0

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        

        # this both counts the fresh fruit and rotten fruit positions
        for row in range(rows):
            for col in range(cols):
                current_pos = grid[row][col]
                if current_pos == 1:
                    fresh_fruit += 1
                if current_pos == 2:
                    queue.append((row, col))
        
        if fresh_fruit == 0:
            return 0

        while queue:

            for i in range(len(queue)):

                r, c = queue.popleft()

                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    if min(dr + r, dc + c) < 0 or dr + r >= rows or dc + c >= cols or grid[dr + r][c + dc] != 1:
                        continue # check next direction, ignore out of bounds, and non rotten fruit positions

                    grid[r + dr][c + dc] = 2
                    queue.append((r + dr, c + dc))
                    rotten += 1
            if queue:
                minutes += 1
        
        if rotten == fresh_fruit:
            return minutes
        
        return -1