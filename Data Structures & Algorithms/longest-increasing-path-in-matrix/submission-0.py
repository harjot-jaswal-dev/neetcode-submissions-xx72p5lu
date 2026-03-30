class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        longest_path = 0
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(r, c):
            
            max_path = 1 # i have trouble understanding how this works 
            moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for move in moves:
                mr, mc = move
                if r + mr < 0 or r + mr >= rows or c + mc < 0 or c + mc >= cols:
                    continue
                if matrix[r][c] >= matrix[r + mr][c + mc]:
                    continue
                
                neighbor = dfs(r + mr, c + mc) # i don't completly understand why we can't do count += dfs, isn't count tracking the path length and as we can go deeper in dfs we increment it

                max_path = max(max_path, 1 + neighbor)
            
            return max_path

        
        for row in range(rows):
            for col in range(cols):
                result = dfs(row, col)
                longest_path = max(longest_path, result)
        
        return longest_path
            

