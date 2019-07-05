"""
980. Unique Paths III (Hard)

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending 
square, that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),
(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),
(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),
(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),
(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),
(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),
(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Note:

1 <= grid.length * grid[0].length <= 20
"""

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i1, j1 = None, None
        i2, j2 = None, None
        h = len(grid)
        w = len(grid[0])
        self.total = 1
        self.result = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    i1, j1 = i, j
                if grid[i][j] == 0:
                    self.total += 1
        visited = set()

        def backtrack(i, j):
            # visit self
            if grid[i][j] == 2:
                if len(visited) == self.total:
                    self.result += 1
                return
            elif grid[i][j] in [0,1]:
                visited.add((i, j))
                if i > 0 and grid[i-1][j] in [0, 2] and (i-1, j) not in visited:
                    backtrack(i-1, j)
                if i < h-1 and grid[i+1][j] in [0, 2] and (i+1, j) not in visited:
                    backtrack(i+1, j)
                if j > 0 and grid[i][j-1] in [0, 2] and (i, j-1) not in visited:
                    backtrack(i, j-1)
                if j < w-1 and grid[i][j+1] in [0, 2] and (i, j+1) not in visited:
                    backtrack(i, j+1)
                visited.remove((i, j))

        backtrack(i1, j1)
        return self.result


if __name__ == "__main__":
    a = Solution()
    print(a.uniquePathsIII([[0,1],[2,0]]))
