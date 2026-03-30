class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        final = 0

        def dfs(r, c):

            if (r, c) in seen:
                return 0
            
            seen.add((r, c))
            counter = 1
            
            moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for move in moves:
                mr, mc = move
                if r + mr < 0 or r + mr >= rows or c + mc < 0 or c + mc >= cols:
                    continue
                if (r + mr, c + mc) in seen or grid[r + mr][c + mc] != 1:
                    continue
                counter += dfs(r + mr, c + mc)

            return counter
        

        for row in range(rows):
            for col in range(cols):
                curr_box = grid[row][col]
                if (row, col) in seen or curr_box != 1:
                    continue
                result = dfs(row, col)
                final = max(final, result)
        
        return final