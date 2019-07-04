"""
695. Max Area of Island (Easy)

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""

class Solution(object):
  def maxAreaOfIsland(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    if m == 0: return 0
    n = len(grid[0])
    if n == 0: return 0

    ones = set()
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          ones.add((i,j))

    result = 0
    while len(ones) != 0:
      # bfs from a random point
      ii, jj = ones.pop()
      stack = [(ii, jj)]
      tmp = 0
      while len(stack) != 0:
        ii, jj = stack.pop()
        # count current
        tmp += 1

        if (ii+1, jj) in ones:
          ones.remove((ii+1, jj))
          stack.append((ii+1, jj))
        if (ii-1, jj) in ones:
          ones.remove((ii-1, jj))
          stack.append((ii-1, jj))
        if (ii, jj+1) in ones:
          ones.remove((ii, jj+1))
          stack.append((ii, jj+1))
        if (ii, jj-1) in ones:
          ones.remove((ii, jj-1))
          stack.append((ii, jj-1))
      result = max(result, tmp)
      print ones
    return result


if __name__ == "__main__":
  a = Solution()
  arr = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
  print a.maxAreaOfIsland(arr)
  arr = [[0,0,0,0,0,0,0,0]]

  print a.maxAreaOfIsland(arr)
