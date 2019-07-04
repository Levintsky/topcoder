"""
694. Number of Distinct Islands (Medium)

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""

class Solution(object):
  def numDistinctIslands(self, grid):
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

    distinct = set()
    while len(ones) > 0:
      # find one
      tmp = []
      new = []
      ii, jj = ones.pop()
      new.append((ii, jj))
      # bfs
      while len(new) > 0:
        ii, jj = new.pop()
        tmp.append((ii, jj))
        if (ii-1, jj) in ones:
          ones.remove((ii-1, jj))
          new.append((ii-1, jj))
        if (ii+1, jj) in ones:
          ones.remove((ii+1, jj))
          new.append((ii+1, jj))
        if (ii, jj-1) in ones:
          ones.remove((ii, jj-1))
          new.append((ii, jj-1))
        if (ii, jj+1) in ones:
          ones.remove((ii, jj+1))
          new.append((ii, jj+1))
      # encode and save
      # print tmp
      tmp.sort()
      off1, off2 = tmp[0]
      tmp = [(item[0]-off1, item[1]-off2) for item in tmp]
      distinct.add(tuple(tmp))
    return len(distinct)


if __name__ == "__main__":
  a = Solution()
  arr = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
  print a.numDistinctIslands(arr)
