from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        count = 0

        for row in range(rows):
            for col in range(cols):
                current_pos = grid[row][col]

                if current_pos == "1" and (row, col) not in visited:
                    count += 1
                    queue = deque([(row, col)])
                    visited.add((row, col))

                    while queue:

                        row, col = queue.popleft()

                        
                        visited.add((row, col))
                        
                        if 0 <= row + 1 < rows and grid[row + 1][col] == "1" and (row + 1, col) not in visited:
                            queue.append((row + 1, col))
                        if 0 <= row - 1 < rows and grid[row - 1][col] == "1" and (row - 1, col) not in visited:
                            queue.append((row - 1, col))
                        if 0 <= col + 1 < cols and grid[row][col + 1] == "1" and (row, col + 1) not in visited:
                            queue.append((row, col + 1))
                        if 0 <= col - 1 < cols and grid[row][col - 1] == "1" and (row, col - 1) not in visited:
                            queue.append((row, col - 1))

        return count
