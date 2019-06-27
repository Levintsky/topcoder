"""
1034. Coloring A Border (Medium)

Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.

Example 1:

Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]

Example 2:

Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]

Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

Note:

1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000
"""


class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        visited = set()
        border = set()
        m = len(grid)
        n = len(grid[0])

        def check(i, j):
            if i == 0 or i == m - 1:
                return True
            if j == 0 or j == n - 1:
                return True
            if i > 0 and grid[i - 1][j] != grid[i][j]:
                return True
            if j > 0 and grid[i][j - 1] != grid[i][j]:
                return True
            if i < m - 1 and grid[i + 1][j] != grid[i][j]:
                return True
            if j < n - 1 and grid[i][j + 1] != grid[i][j]:
                return True
            return False

        stack = [(r0, c0)]
        while len(stack) > 0:
            ii, jj = stack.pop()
            visited.add((ii, jj))
            if check(ii, jj):
                border.add((ii, jj))
            if (
                ii > 0
                and grid[ii - 1][jj] == grid[ii][jj]
                and (ii - 1, jj) not in visited
            ):
                stack.append((ii - 1, jj))
            if (
                ii < m - 1
                and grid[ii + 1][jj] == grid[ii][jj]
                and (ii + 1, jj) not in visited
            ):
                stack.append((ii + 1, jj))
            if (
                jj > 0
                and grid[ii][jj - 1] == grid[ii][jj]
                and (ii, jj - 1) not in visited
            ):
                stack.append((ii, jj - 1))
            if (
                jj < n - 1
                and grid[ii][jj + 1] == grid[ii][jj]
                and (ii, jj + 1) not in visited
            ):
                stack.append((ii, jj + 1))
        # print(border)
        for i, j in border:
            grid[i][j] = color
        return grid


if __name__ == "__main__":
    a = Solution()
    print(a.colorBorder([[1, 1], [1, 2]], 0, 0, 3))
    print(a.colorBorder([[1, 2, 2], [2, 3, 2]], 0, 1, 3))
    print(a.colorBorder([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2))
    print(a.colorBorder([[3, 2, 2, 2], [2, 3, 3, 3], [1, 3, 1, 2]], 0, 1, 1))
