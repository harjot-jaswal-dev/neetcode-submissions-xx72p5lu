class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if board is None or word is None:
            return False
        
        letter_tracker = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            
            if board[r][c] != word[index] or (r, c) in letter_tracker:
                return False # after this we know board[r][c] matches the word[index]
            
            index += 1

            if index == len(word):
                return True

            letter_tracker.add((r, c))

            moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for move in moves:
                mr, mc = move
                if r + mr < 0 or r + mr >= rows or c + mc < 0 or c + mc >= cols:
                    continue
                elif dfs(r + mr, c + mc, index):
                    return True
        
            letter_tracker.remove((r, c))

            return False
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        
        return False



