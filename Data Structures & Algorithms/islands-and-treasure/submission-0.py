from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))
        
        distance = 0

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()

                if grid[r][c] == 2147483647:
                    grid[r][c] = distance
                
                moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for move in moves:
                    mr, mc = move
                    if r + mr < 0 or r + mr >= rows or c + mc < 0 or c + mc >= cols:
                        continue
                    if (r + mr, c + mc) in visited or grid[r + mr][c + mc] != 2147483647:
                        continue # can't add dupes and non land cells
                    queue.append((r + mr, c + mc))
                    visited.add((r + mr, c + mc))
            distance += 1
        
                    
