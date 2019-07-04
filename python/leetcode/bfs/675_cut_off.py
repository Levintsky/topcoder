"""
675. Cut Off Trees for Golf Event (Hard)

You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6

Example 2:
Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
Example 3:
Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
Hint: size of the given matrix will not exceed 50x50.
"""

import heapq
import collections

class Solution(object):
  def cutOffTree(self, forest):
    """
    :type forest: List[List[int]]
    :rtype: int
    """
    m = len(forest)
    if m == 0: return 0
    n = len(forest[0])
    if n == 0: return 0

    heap = []
    for i in range(m):
      for j in range(n):
        if forest[i][j] > 1:
          # heapq.heappush(heap, (forest[i][j], i,j))
          heap.append((forest[i][j], i, j))
    heap.sort()
    print heap

    # bfs
    result = 0
    cx, cy = 0, 0
    # _, cx, cy = heap[0]
    while len(heap) > 0:
      weight, i, j = heapq.heappop(heap)
      print weight, i, j
      # bfs from curr
      step = self.bfs(forest, cx, cy, i, j)
      print step
      if step == -1: return -1
      forest[i][j] = 1
      cx, cy = i, j
      result += step
    return result

  def bfs(self, forest, cx, cy, tx, ty):
    if cx == tx and cy == ty: return 0

    m, n = len(forest), len(forest[0])
    visited = set()
    visited.add((cx,cy))
    q1 = collections.deque()
    q1.append((cx,cy))
    step = 0
    while len(q1) > 0:
      q2 = collections.deque()
      step += 1
      while len(q1) > 0:
        x, y = q1.popleft()
        if x > 0 and forest[x-1][y]!=0 and (x-1,y) not in visited: # and forest[x-1][y] <= forest[tx][ty]:
          q2.append((x-1,y))
          visited.add((x-1,y))
        if x < m-1 and forest[x+1][y]!=0 and (x+1,y) not in visited: # and forest[x+1][y] <= forest[tx][ty]:
          q2.append((x+1,y))
          visited.add((x+1,y))
        if y > 0 and forest[x][y-1]!=0 and (x,y-1) not in visited: # and forest[x][y-1] <= forest[tx][ty]:
          q2.append((x,y-1))
          visited.add((x,y-1))
        if y < n-1 and forest[x][y+1]!=0 and(x,y+1) not in visited: # and forest[x][y+1] <= forest[tx][ty]:
          q2.append((x,y+1))
          visited.add((x,y+1))
      print step, visited
      if (tx,ty) in visited: return step
      if len(q2) == 0: return -1
      q1 = q2


if __name__ == "__main__":
  a = Solution()
  print a.cutOffTree([
 [1,2,3],
 [0,0,4],
 [7,6,5]
])
  print 'new'
  print a.cutOffTree([
 [1,2,3],
 [0,0,0],
 [7,6,5]
])
  print 'new'
  print a.cutOffTree([
 [2,3,4],
 [0,0,5],
 [8,7,6]
])
  print 'new'
  print a.cutOffTree([[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]])
