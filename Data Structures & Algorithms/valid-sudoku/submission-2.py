class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = len(board)

        row_check = {}
        col_check = {}
        sub_check = {}

        for row in range(n):
            for col in range(n):
                cell = board[row][col]
                
                if cell == ".":
                    continue
                
                # Check row
                if row not in row_check:
                    row_check[row] = []
                if cell in row_check[row]:
                    return False
                row_check[row].append(cell)
                
                # Check column
                if col not in col_check:
                    col_check[col] = []
                if cell in col_check[col]:
                    return False
                col_check[col].append(cell)
                
                # Check 3x3 box (your code)
                section = (row // 3, col // 3)
                if section not in sub_check:
                    sub_check[section] = []
                if cell in sub_check[section]:
                    return False
                sub_check[section].append(cell)
    
        return True



   

                 


        
        