"""
840. Magic Squares In Grid (Easy)

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def check_magic(i, j):
            # check distinct
            set_ = set()
            for ii in range(i, i + 3):
                for jj in range(j, j + 3):
                    set_.add(grid[ii][jj])
            if not len(set_) == 9 or min(set_) != 1 or max(set_) != 9:
                return False
            # check sum
            for ii in range(i, i + 3):
                sum_ = sum(grid[ii][j : j + 3])
                if sum_ != 15:
                    return False
            for jj in range(j, j + 3):
                sum_ = sum([grid[ii][jj] for ii in range(i, i + 3)])
                if sum_ != 15:
                    return False
            if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15:
                return False
            if grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] != 15:
                return False
            return True

        result = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if check_magic(i, j):
                    print(i, j)
                    result += 1
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
