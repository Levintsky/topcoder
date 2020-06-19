"""
1293. Shortest Path in a Grid with Obstacles Elimination (Hard)

Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
"""

import collections


class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        memo = set()
        memo.add((0, 0, k))
        
        q = collections.deque()
        q.append((0, 0, k)) # i, j, k-remain
        
        m, n = len(grid), len(grid[0])
        
        step = 0
        
        while len(q) > 0:
            q2 = set()
            
            while len(q) > 0:
                i, j, kk = q.popleft()
                memo.add((i, j, kk))
                if (i, j) == (m-1, n-1):
                    return step
            
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ii, jj = i+di, j+dj
                    if ii < 0 or jj < 0 or ii >=m or jj >= n:
                        continue
                    new_k = kk - grid[ii][jj]
                    if new_k < 0:
                        continue
                    # check (ii, jj, new_k)
                    flag = True
                    for tmp_k in range(new_k, k+1):
                        if (ii, jj, tmp_k) in memo:
                            flag = False
                            break
                    if flag:
                        q2.add((ii, jj, new_k))
            # move q2 to q
            for item in q2:
                q.append(item)
            step += 1
        return -1


if __name__ == "__main__":
    a = Solution()
    grid = [[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]]
    print(a.shortestPath(grid, 1))
    grid = [[0,1,1],
 [1,1,1],
 [1,0,0]]
    print(a.shortestPath(grid, 1))

                