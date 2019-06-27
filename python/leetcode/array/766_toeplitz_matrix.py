"""
766. Toeplitz Matrix (Easy)

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:
asdf
What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""

"""
super smart idea:
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length - 1; i++) {
            for (int j = 0; j < matrix[i].length - 1; j++) {
                if (matrix[i][j] != matrix[i + 1][j + 1]) return false;
            }
        }
        return true;
    }
}
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return True
        n = len(matrix[0])
        if n == 0:
            return True
        # from left-bottom, [m-1][0]
        # to right-top, [0][n-1]
        diff = m - 1
        while diff >= 1 - n:
            if diff >= 0:
                max_ = min(m - diff, n)
                data = [matrix[diff + idx][idx] for idx in range(0, max_)]
            else:
                diff2 = -diff
                max_ = min(m, n + diff)
                # print(-diff, max_)
                data = [matrix[idx][idx + diff2] for idx in range(0, max_)]
            # print(diff, -diff, data)
            dataset = set(data)
            if len(dataset) >= 2:
                return False
            diff -= 1
        return True


if __name__ == "__main__":
    a = Solution()
    # matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    matrix = [[97, 97], [80, 97], [10, 80]]
    print(a.isToeplitzMatrix(matrix))
