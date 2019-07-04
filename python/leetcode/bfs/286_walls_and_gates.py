"""
286. Walls and Gates (Medium)

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""

class Solution(object):
  def wallsAndGates(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: void Do not return anything, modify rooms in-place instead.
    """
    # step 1: find current 0s
    curr = []
    new = []
    m = len(rooms)
    if m == 0: return
    n = len(rooms[0])
    if n == 0: return

    for i in range(m):
      for j in range(n):
        if rooms[i][j] == 0:
          curr.append((i, j))

    step = 1
    while len(curr) > 0:
      while len(curr) > 0:
        i, j = curr.pop()
        if i > 0 and rooms[i-1][j] > m * n:
          rooms[i-1][j] = step
          new.append((i-1, j))
        if i < m - 1 and rooms[i+1][j] > m * n:
          rooms[i+1][j] = step
          new.append((i+1, j))
        if j > 0 and rooms[i][j-1] > m * n:
          rooms[i][j-1] = step
          new.append((i, j-1))
        if j < n - 1 and rooms[i][j+1] > m * n:
          rooms[i][j+1] = step
          new.append((i, j+1))
      curr, new = new, []
      step += 1
    return 


if __name__ == "__main__":
  a = Solution()
  INF = 2 ** 31 - 1
  arr = [[INF, -1,   0, INF],
         [INF, INF, INF, -1],
         [INF, -1,  INF, -1],
         [0,   -1,  INF, INF]]
  a = Solution()
  a.wallsAndGates(arr)
  print arr
