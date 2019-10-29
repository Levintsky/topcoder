"""
1219. Path with Maximum Gold (Medium)

In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.best = 0
        visited = set()
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, curr):
            visited.add((i, j))
            curr += grid[i][j]
            
            for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                ii, jj = i + di, j+dj
                if ii >= 0 and ii < m and jj >= 0 and jj < n and grid[ii][jj] > 0 and (ii, jj) not in visited:
                    dfs(ii, jj, curr)
            self.best = max(self.best, curr)
            curr -= grid[i][j]
            visited.remove((i, j))
            return
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        return self.best

    def solve2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.best = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j, curr):
            m, n = len(grid), len(grid[0])
            curr += grid[i][j]
            tmp = grid[i][j]
            grid[i][j] = 0
            
            if i > 0 and grid[i-1][j] > 0:
                dfs(i-1, j, curr)
            if i < m-1 and grid[i+1][j] > 0:
                dfs(i+1, j, curr)
            if j > 0 and grid[i][j-1] > 0:
                dfs(i, j-1, curr)
            if j < n-1 and grid[i][j+1] > 0:
                dfs(i, j+1, curr)
            self.best = max(self.best, curr)
            curr -= tmp
            grid[i][j] = tmp
            return
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        return self.best


if __name__ == "__main__":
    a = Solution()
    print(a.solve2([[0,6,0],[5,8,7],[0,9,0]]))
