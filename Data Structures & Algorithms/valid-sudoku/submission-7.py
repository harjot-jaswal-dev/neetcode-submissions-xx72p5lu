class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_check = {}
        col_check = {}
        box_check = {}

        for row in range(9):
            for col in range(9):
                curr_box = board[row][col]

                # row check
                if row not in row_check:
                    row_check[row] = []
                if curr_box in row_check[row]:
                    return False
                if curr_box != ".":
                    row_check[row].append(curr_box)
                
                # col check
                if col not in col_check:
                    col_check[col] = []
                if curr_box in col_check[col]:
                    return False
                if curr_box != ".":
                    col_check[col].append(curr_box)
                
                # box check
                box = (row // 3) * 3 + col // 3
                if box not in box_check:
                    box_check[box] = []
                if curr_box in box_check[box]:
                    return False
                if curr_box != ".":
                    box_check[box].append(curr_box)

        
        return True

                
