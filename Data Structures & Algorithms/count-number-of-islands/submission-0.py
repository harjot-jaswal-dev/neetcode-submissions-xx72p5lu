class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        # dfs helper
        visited = set()
        count = 0

        def dfs(grid, r, c, visited):

            if r < 0 or r >= rows or c < 0 or c >= cols: # out of bounds check
                return 
            
            if grid[r][c] == "0" or (r, c) in visited:
                return 
            
            if (r, c) not in visited:
                visited.add((r, c))
                

           
            dfs(grid, r + 1, c, visited)
            dfs(grid, r - 1, c, visited)
            dfs(grid, r, c + 1, visited)
            dfs(grid, r, c - 1, visited)

        for row in range(rows):
            for col in range(cols):
                current_pos = grid[row][col]
                if (row, col) not in visited and current_pos == "1":
                    count += 1
                    dfs(grid, row, col, visited)

        return count

    



