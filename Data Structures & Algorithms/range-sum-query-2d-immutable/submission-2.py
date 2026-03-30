class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows, cols = len(matrix), len(matrix[0])
        self.prefix = []

        for i in range(rows):
            row = []
            for y in range(cols):
                row.append(0)
            self.prefix.append(row)
        
        for row in range(rows):
            for col in range(cols):
                if row > 0 and col > 0:
                    self.prefix[row][col] = self.prefix[row - 1][col] + self.prefix[row][col - 1] + matrix[row][col] - self.prefix[row - 1][col - 1]
                elif row > 0: # only on 2nd row but 1st col
                    self.prefix[row][col] = self.prefix[row - 1][col] + matrix[row][col]
                elif col > 0: # on first row and col > 0
                    self.prefix[row][col] = self.prefix[row][col - 1] + matrix[row][col]
                else: # both col and row == 0
                    self.prefix[row][col] = matrix[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = self.prefix[row2][col2]

        if row1 > 0 and col1 > 0:
            res -= self.prefix[row1 - 1][col2] + self.prefix[row2][col1 - 1] - self.prefix[row1 - 1][col1 - 1]
        elif row1 > 0:
            res -= self.prefix[row1 - 1][col2] 
        elif col1 > 0:
            res -= self.prefix[row2][col1 - 1]
        
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)