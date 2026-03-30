class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        max_area = []

        def dfs(grid, r, c, visited):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            
            if (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            count = 1

            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r, c - 1, visited)

            return count


        for row in range(rows):
            for col in range(cols):
                current_pos = grid[row][col]
                if current_pos == 1 and (row, col) not in visited:
                    area = dfs(grid, row, col, visited)
                    max_area.append(area)

        if len(max_area) <= 0:
            return 0

        return max(max_area)