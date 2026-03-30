class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = []

        for row in range(rows + 1): # initalizes self.prefix
            res = []
            for col in range(cols + 1):
                res.append(0)
            self.prefix.append(res)
        
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                self.prefix[row][col] = matrix[row - 1][col - 1] + self.prefix[row - 1][col] + self.prefix[row][col - 1] - self.prefix[row - 1][col - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row2 += 1
        col2 += 1
        row1 += 1
        col1 += 1
        res = self.prefix[row2][col2]

        res -= self.prefix[row1 - 1][col2] + self.prefix[row2][col1 - 1] - self.prefix[row1 - 1][col1 - 1]

        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)