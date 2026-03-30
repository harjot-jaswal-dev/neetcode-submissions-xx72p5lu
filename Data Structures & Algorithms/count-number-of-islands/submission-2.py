class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        total = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def dfs(r, c):

            if (r, c) in seen:
                return 0
            
            seen.add((r, c))

            moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for move in moves:
                mr, mc = move
                if r + mr < 0 or r + mr >= rows or c + mc < 0 or c + mc >= cols:
                    continue # out of bounds
                if (r + mr, c + mc) in seen or grid[r + mr][c + mc] != "1":
                    continue # already seen or not land
                
                dfs( r + mr, c + mc)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "1" or (row, col) in seen:
                    continue
                dfs(row, col)
                total += 1
        
        return total