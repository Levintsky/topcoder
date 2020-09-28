"""
1594. Maximum Non Negative Product in a Matrix (Medium)

You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (rows - 1, cols - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:

Input: grid = [[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]
Output: -1
Explanation: It's not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:

Input: grid = [[1,-2,1],
               [1,-2,1],
               [3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is in bold (1 * 1 * -2 * -4 * 1 = 8).
Example 3:

Input: grid = [[1, 3],
               [0,-4]]
Output: 0
Explanation: Maximum non-negative product is in bold (1 * 0 * -4 = 0).
Example 4:

Input: grid = [[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]
Output: 2
Explanation: Maximum non-negative product is in bold (1 * -2 * 1 * -1 * 1 * 1 = 2).
 

Constraints:

1 <= rows, cols <= 15
-4 <= grid[i][j] <= 4
"""

import pdb

class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m):
            tmp = [(0, 0)] * n
            res.append(tmp)

        if grid[0][0] > 0:
            res[0][0] = (grid[0][0], 0)
        else:
            res[0][0] = (0, grid[0][0])

        z_flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    z_flag = True

        for step in range(1, m+n-1):
            for i in range(step+1):
                j = step - i
                if i < m and j < n:
                    curr = grid[i][j]
                    # with left
                    if j > 0:
                        if curr > 0:
                            r1 = max(res[i][j][0], res[i][j-1][0] * curr)
                            r2 = min(res[i][j][1], res[i][j-1][1] * curr)
                        else:
                            r1 = max(res[i][j][0], res[i][j-1][1] * curr)
                            r2 = min(res[i][j][1], res[i][j-1][0] * curr)
                        res[i][j] = (r1, r2)
                    # with up
                    if i > 0:
                        if curr > 0:
                            r1 = max(res[i][j][0], res[i-1][j][0] * curr)
                            r2 = min(res[i][j][1], res[i-1][j][1] * curr)
                        else:
                            r1 = max(res[i][j][0], res[i-1][j][1] * curr)
                            r2 = min(res[i][j][1], res[i-1][j][0] * curr)
                        res[i][j] = (r1, r2)
        MOD = 10 ** 9 + 7
        if res[m-1][n-1][0] > 0:
            return res[m-1][n-1][0] % MOD
        elif z_flag:
            return 0
        else: # res[m-1][n-1][1] < 0:
            return -1
        # else:
        #     return 0


if __name__ == "__main__":
    a = Solution()
    # pdb.set_trace()
    print(a.maxProductPath([[-1,-2,-3],
               [-2,-3,-3],
               [-3,-3,-2]]))
    print(a.maxProductPath([[1,-2,1],
               [1,-2,1],
               [3,-4,1]]))
    print(a.maxProductPath([[1, 3],
               [0,-4]]))
    print(a.maxProductPath([[ 1, 4,4,0],
               [-2, 0,0,1],
               [ 1,-1,1,1]]))
