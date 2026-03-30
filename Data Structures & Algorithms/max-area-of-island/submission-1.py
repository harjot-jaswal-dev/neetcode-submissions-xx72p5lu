class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if grid is None:
            return 0

        visited = set()
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):

            if (r, c) in visited:
                return 0 # check if neighbor is repeated 
            
            if grid[r][c] != 1:
                return 0 # check if neighbor is part of island
            
            count = 1 # its is part of island count += 1
            visited.add((r, c)) # add neighbor to vsisted
            moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for move in moves:
                change_r, change_c = move
                if r + change_r < 0 or r + change_r >= rows or c + change_c < 0 or c + change_c >= cols:
                    continue # out of bounds
                count += dfs(r + change_r, c + change_c)

            return count # after looking at all possible neighbors return count
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col)) # compare current to dfs count take the bigger number
        
        return max_area