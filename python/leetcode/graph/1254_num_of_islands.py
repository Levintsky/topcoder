"""
1254. Number of Closed Islands
Medium

200

12

Add to List

Share
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""

import collections

class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            flag = 1
            while len(q) > 0:
                ii, jj = q.popleft()
                if grid[ii][jj] > 0:
                    continue
                if ii == 0 or ii == m-1 or jj == 0 or jj == n-1:
                    flag = 0
                grid[ii][jj] = 2
                if ii > 0 and grid[ii-1][jj] == 0:
                    q.append((ii-1, jj))
                if ii < m-1 and grid[ii+1][jj] == 0:
                    q.append((ii+1, jj))
                if jj > 0 and grid[ii][jj-1] == 0:
                    q.append((ii, jj-1))
                if jj < n-1 and grid[ii][jj+1] == 0:
                    q.append((ii, jj+1))
            return flag

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    result += bfs(i, j)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.closedIsland( [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
    print(a.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
    print(a.closedIsland([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]))