"""
1536. Minimum Swaps to Arrange a Binary Grid (Medium)

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 200
grid[i][j] is 0 or 1
"""

class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = []
        for tgrid in grid:
            tmp = 0
            for item in tgrid[::-1]:
                if item == 0:
                    tmp += 1
                else:
                    break
            memo.append(tmp)
        
        # bubble sort
        n = len(grid)
        res = 0
        for idx in range(n-1):
            req = n - 1 - idx
            idx2 = 0
            while idx2 < len(memo) and memo[idx2] < req:
                idx2 += 1
            if idx2 == len(memo):
                return -1
            res += idx2
            memo = memo[:idx2] + memo[idx2+1:]
        return res
        
