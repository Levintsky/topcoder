"""
994. Rotting Oranges (Easy)

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        clean_set = set()
        result = 0
        rot_set = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rot_set.append((i, j))
                elif grid[i][j] == 1:
                    clean_set.add((i, j))
        if len(clean_set) == 0:
            return 0

        # bfs
        while len(rot_set) > 0:
            tmp_set = deque()
            while len(rot_set) > 0:
                i, j = rot_set.pop()
                grid[i][j] = 2
                if i > 0 and grid[i - 1][j] == 1 and (i - 1, j) in clean_set:
                    tmp_set.append((i - 1, j))
                    clean_set.remove((i - 1, j))
                if i < m - 1 and grid[i + 1][j] == 1 and (i + 1, j) in clean_set:
                    tmp_set.append((i + 1, j))
                    clean_set.remove((i + 1, j))
                if j > 0 and grid[i][j - 1] == 1 and (i, j - 1) in clean_set:
                    tmp_set.append((i, j - 1))
                    clean_set.remove((i, j - 1))
                if j < n - 1 and grid[i][j + 1] == 1 and (i, j + 1) in clean_set:
                    tmp_set.append((i, j + 1))
                    clean_set.remove((i, j + 1))
            result += 1
            rot_set = tmp_set
        if len(clean_set) == 0:
            return result - 1
        else:
            return -1


if __name__ == "__main__":
    a = Solution()
    array = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(a.orangesRotting(array))
    array = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(a.orangesRotting(array))
    array = [[0, 2]]
    print(a.orangesRotting(array))
