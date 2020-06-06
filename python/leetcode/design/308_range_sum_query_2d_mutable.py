"""
308. Range Sum Query 2D - Mutable (Hard)

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
 

Note:

The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 <= row2 and col1 <= col2.
"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        if n == 0: return
        # matrix
        self.matrix = []
        for i in range(m):
            self.matrix.append([0] * n)
        
        # binary index tree
        self.bit = []
        # init
        for i in range(m + 1):
            self.bit.append([0] * (n + 1))
        # update
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        m, n = len(self.matrix), len(self.matrix[0])
        while i <= m:
            j = col + 1
            while j <= n:
                self.bit[i][j] += delta
                j += j & (-j)
            i += i & (-i)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        A = self.helper(row2, col2)
        B = self.helper(row1 - 1, col2)
        C = self.helper(row2, col1 - 1)
        D = self.helper(row1 - 1, col1 - 1)
        return A + D - B - C
    
    def helper(self, row, col):
        result = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                result += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == "__main__":
    obj = NumMatrix([[1]])
    print obj.bit
    print obj.sumRegion(0, 0, 0, 0)
    obj.update(0, 0, -1)
    print obj.bit
    print obj.sumRegion(0, 0, 0, 0)
