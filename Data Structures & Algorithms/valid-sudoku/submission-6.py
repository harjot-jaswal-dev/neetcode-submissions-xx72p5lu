class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_check = {}
        col_check = {}
        box_check = {}

        for row in range(len(board)):
            for col in range(len(board)):
                cell = board[row][col]
                if cell == ".":
                    continue

                if row not in row_check:
                    row_check[row] = []
                elif cell in row_check[row]:
                    return False
                row_check[row].append(cell)

                if col not in col_check:
                    col_check[col] = []
                elif cell in col_check[col]:
                    return False
                col_check[col].append(cell)

                current_box = (row // 3, col // 3)
                if current_box not in box_check:
                    box_check[current_box] = []
                elif cell in box_check[current_box]:
                    return False
                box_check[current_box].append(cell)
        return True


            