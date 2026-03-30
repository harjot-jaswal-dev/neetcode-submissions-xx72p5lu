class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights:
            return None
        
        pacific_cells = set()
        atlantic_cells = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs_pacific(r, c):

            if (r, c) in pacific_cells:
                return

            pacific_cells.add((r, c))

            moves = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for move in moves:
                move_r, move_c = move
                if r + move_r < 0 or r + move_r >= rows or c + move_c < 0 or c + move_c >= cols:
                    continue # out of bounds
                if heights[move_r + r][move_c + c] < heights[r][c]:
                    continue # only want equal or higher adj nodes
                dfs_pacific(r + move_r, c + move_c)
        
        def dfs_atlantic(r, c):

            if (r, c) in atlantic_cells:
                return

            atlantic_cells.add((r, c))

            moves = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for move in moves:
                move_r, move_c = move
                if r + move_r < 0 or r + move_r >= rows or c + move_c < 0 or c + move_c >= cols:
                    continue # out of bounds
                if heights[move_r + r][move_c + c] < heights[r][c]:
                    continue # only want equal or higher adj nodes
                dfs_atlantic(r + move_r, c + move_c)

        

        # left col/left pacific
        for i in range(rows):
            dfs_pacific(i, 0)
        
        # row 1/top pacific
        for i in range(cols):
            dfs_pacific(0, i)
        
        # left col/right atlantic
        for i in range(rows):
            dfs_atlantic(i, cols - 1)
        
        # bottom row, bottom atlantic
        for i in range(cols):
            dfs_atlantic(rows - 1, i)
        
        return list(pacific_cells & atlantic_cells)