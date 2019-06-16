"""
1091. Shortest Path in Binary Matrix (Medium)

In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Example 1:

Input: [[0,1],[1,0]]
Output: 2
Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1

"""

from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1: return -1
        if grid[-1][-1] == 1: return -1
        k = len(grid[0])
        grid[0][0] = -1
        q = deque()
        q.append((0, 0))
        curr = -2
        while len(q) > 0:
            q2 = deque()
            while len(q) > 0:
                i, j = q.popleft()
                for ii in range(max(0, i-1), min(i+2,k)):# [i-1, i, i+1]:
                    for jj in range(max(0, j-1), min(j+2,k)):
                        if ii != i or jj != j:
                            if grid[ii][jj] == 0:
                                grid[ii][jj] = curr
                                q2.append((ii, jj))
            q = q2
            curr -= 1
        print(grid)
        if grid[-1][-1] == 0:
            return -1
        else:
            return -grid[-1][-1]


if __name__ == "__main__":
    a = Solution()
    print(a.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(a.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))