"""
1162. As Far from Land as Possible (Medium)

Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

Example 1:
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: 
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: 
The cell (2, 2) is as far as possible from all the land with distance 4.

Note:

1 <= grid.length == grid[0].length <= 100
grid[i][j] is 0 or 1

"""

import collections

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q1 = collections.deque()
        m = len(grid)
        if m == 0: return -1
        n = len(grid[0])
        if n == 0: return -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q1.append((i, j))
        if len(q1) == 0 or len(q1) == m * n:
            return -1
        curr = 2
        res = 0
        while q1:
            q2 = collections.deque()
            while q1:
                i, j = q1.popleft()
                for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    newi, newj = i+ii, j+jj
                    if newi >= 0 and newi < m and newj >= 0 and newj < n and grid[newi][newj] == 0:
                        grid[newi][newj] = curr
                        res = curr - 1
                        q2.append((newi, newj))
            curr += 1
            q1 = q2
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
    print(a.maxDistance([[1,0,0,0],[0,0,0,0],[0,0,0,0]]))
