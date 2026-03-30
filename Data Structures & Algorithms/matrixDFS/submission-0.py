class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        total = 0

        def dfs(grid, r, c, visited):

            if r < 0 or r >= rows or c < 0 or c >= cols: # out of bounds check
                return 0
            
            if grid[r][c] == 1 or (r, c) in visited: # rocks and visited check
                return 0
            
            if r == rows - 1 and c == cols - 1 and grid[r][c] == 0:
                return 1
            
            visited.add((r, c))

            count = 0
            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r, c - 1, visited)

            visited.remove((r, c))

            return count

        total += dfs(grid, 0, 0, visited)
        return total