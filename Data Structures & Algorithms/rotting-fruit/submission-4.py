class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if grid is None:
            return -1
        
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh_oranges = 0
        minute = 0

        # counted all fresh oranges and all starting rotten oranges in queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        
        if fresh_oranges == 0:
            return 0

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()

                moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for move in moves:
                    mr, mc = move
                    if mr + r < 0 or mr + r >= rows or c + mc < 0 or c + mc >= cols:
                        continue # out of bounds
                    if grid[mr + r][mc + c] != 1:
                        continue # not fresh so we can't rotten
                    # we know at this point it's valid position and not rotten so we add to queue
                    grid[mr + r][c + mc] = 2
                    queue.append((r + mr, c + mc))
                    fresh_oranges -= 1
            if queue:
                minute += 1
        
        if fresh_oranges == 0:
            return minute
        else:
            return -1