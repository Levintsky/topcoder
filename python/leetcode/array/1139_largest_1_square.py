"""
1139. Largest 1-Bordered Square (Medium)

Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
"""

class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0

        rows = []
        cols = []
        for i in range(m):
            rows.append([0] * n)
            cols.append([0] * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if j == 0:
                        rows[i][j] = 1
                    else:
                        rows[i][j] = rows[i][j-1] + 1
                    if i == 0:
                        cols[i][j] = 1
                    else:
                        cols[i][j] = cols[i-1][j] + 1
        print(rows)
        print(cols)

        res = 0
        for i in range(m):
            for j in range(n):
                top = min(i+1, j+1)
                side = top
                while side >= res + 1:
                    if rows[i][j] >= side and cols[i][j] >= side and rows[i-side+1][j] >= side and cols[i][j-side+1] >= side:
                        res = side
                        break
                    side -= 1
        return res ** 2

if __name__ == "__main__":
    a = Solution()
    print(a.largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))
    print(a.largest1BorderedSquare([[1,1,0,0]]))