from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        if grid[0][0] != 0:
            return -1

        queue = deque([(0, 0)]) # we start at (0,0)

        visited.add((0, 0)) 
        length = 1

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()
                
                if r == rows - 1 and c == cols - 1:
                    return length
                
                if 0 <= r + 1 < rows and grid[r + 1][c] == 0 and (r + 1, c) not in visited:
                    queue.append((r + 1, c))
                    visited.add((r + 1, c))
                if 0 <= r - 1 < rows and grid[r -1][c] == 0 and (r - 1, c) not in visited:
                    queue.append((r - 1, c))
                    visited.add((r - 1, c))
                if 0 <= c + 1 < cols and grid[r][c + 1] == 0 and (r, c + 1) not in visited:
                    queue.append((r , c + 1))
                    visited.add((r, c + 1))
                if 0 <= c - 1 < cols and grid[r][c -1] == 0 and (r, c - 1) not in visited:
                    queue.append((r, c - 1))
                    visited.add((r, c - 1))
                if 0 <= r - 1 < rows and 0 <= c - 1 < cols and grid[r -1][c -1] == 0 and (r -1, c -1) not in visited:
                    queue.append((r -1, c -1))
                    visited.add((r -1, c -1))
                if 0 <= r + 1 < rows and 0 <= c + 1 < cols and grid[r + 1][c + 1] == 0 and (r + 1, c + 1) not in visited:
                    queue.append((r + 1, c + 1))
                    visited.add((r + 1, c + 1))
                if 0 <= r + 1 < rows and 0 <= c - 1 < cols and grid[r + 1][c - 1] == 0 and (r + 1, c - 1) not in visited:
                    queue.append((r + 1, c - 1))
                    visited.add((r + 1, c - 1))
                if 0 <= r - 1 < rows and 0 <= c + 1 < cols and grid[r - 1][c + 1] == 0 and (r - 1, c + 1) not in visited:
                    queue.append((r - 1, c + 1))
                    visited.add((r - 1, c + 1))


            length += 1
        
        return -1
        
            
                
            