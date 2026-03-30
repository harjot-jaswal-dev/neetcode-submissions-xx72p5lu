class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows_tracker = {}
        columns_tracker = {}
        box_check = {}

        for row in range(len(board)):
            for col in range(len(board)):

                cell = board[row][col]

                if cell == ".":
                    continue # next cell this cell is fine/considered empty
                
                if row not in rows_tracker: # if this row is not in the rows dict
                    rows_tracker[row] = []
                if cell in rows_tracker[row]: # if this cell has already been in this row then return false, ex) 1,2,3,4,5,6,7,1 this check would catch the extra 1
                    return False
                rows_tracker[row].append(cell)

                if col not in columns_tracker:
                    columns_tracker[col] = []
                if cell in columns_tracker[col]:
                    return False
                columns_tracker[col].append(cell)

                current_box = (row // 3, col // 3)
                if current_box not in box_check:
                    box_check[current_box] = []
                if cell in box_check[current_box]:
                    return False
                box_check[current_box].append(cell)
        return True