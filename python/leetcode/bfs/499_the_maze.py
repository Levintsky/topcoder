"""
499. The Maze II (Hard)

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, your job is to find out how the ball could drop into the hole by moving shortest distance in the maze. The distance is defined by the number of empty spaces the ball go through from the start position (exclude) to the hole (include). Output the moving directions by using 'u', 'd', 'l' and 'r'. Since there may have several different shortest ways, you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The ball and hole coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"
Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. So the output is "lul".

Example 2

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)
Output: "impossible"
Explanation: The ball cannot reach the hole.

Note:

1. There are only one ball and one hole in the maze.
2. The ball and hole will only exist in the empty space, and they will not at the same position initially.
3. The given maze doesn't contain border (like the red rectangle in the example pictures), but you should assume the border of the maze are all walls.
4. The maze contains at least 2 empty spaces, and the length and width of the maze won't exceed 30.
"""

class Solution(object):
  def findShortestWay(self, maze, ball, hole):
    """
    :type maze: List[List[int]]
    :type ball: List[int]
    :type hole: List[int]
    :rtype: str
    """
    visited = {} # (i,j) to [distance, str]
    m = len(maze)
    n = len(maze[0])
    visited[ball] = (0, '')
    last = [ball]
    new = []
    cnt = 0
    while len(last)!=0:
      # bfs, add neighbors to new[] and visited
      for item in last:
        i, j = item
        print 'visiting', i, j
        dis, s = visited[(i,j)]
        # up until (0,j)
        if i>0:
          if len(s) == 0 or s[-1]!='u': s2 = s + 'u'
          else: s2 = s
          ii = i - 1
          while ii>=0 and maze[ii][j] == 0:
            if (ii,j) not in visited:
              visited[(ii,j)] = (dis+i-ii, s2)
            elif visited[(ii,j)][0] == dis+i-ii: visited[(ii,j)] = (dis+i-ii, min(s2, visited[(ii,j)][1]))
            ii -= 1
          ii += 1
          if ii < i and visited[(ii,j)]==(dis+i-ii,s2): new.append((ii,j))
        # down until (0,j)
        if i<m-1:
          if len(s) == 0 or s[-1]!='d': s2 = s + 'd'
          else: s2 = s
          ii = i + 1
          while ii<m and maze[ii][j] == 0:
            if (ii,j) not in visited:
              visited[(ii,j)] = (dis+ii-i, s2)
            elif visited[(ii,j)][0] == dis+ii-i: visited[(ii,j)] = (dis+ii-i, min(s2, visited[(ii,j)][1]))
            ii += 1
          ii -= 1
          if ii>i and visited[(ii,j)]==(dis+ii-i,s2): new.append((ii,j))
        # left until (i,0)
        if j>0:
          if len(s) == 0 or s[-1]!='l': s2 = s + 'l'
          else: s2 = s
          jj = j-1
          while jj>=0 and maze[i][jj] == 0:
            if (i,jj) not in visited:
              visited[(i,jj)] = (dis+j-jj, s2)
            elif visited[(i,jj)][0] == dis+j-jj: visited[(i,jj)] = (dis+j-jj, min(s2, visited[(i,jj)][1]))
            jj -= 1
          jj += 1
          if jj<j and visited[(i,jj)]==(dis+j-jj,s2): new.append((i,jj))
        if j<n-1:
          if len(s) == 0 or s[-1]!='r': s2 = s + 'r'
          else: s2 = s
          jj = j+1
          while jj<n and maze[i][jj] == 0:
            if (i,jj) not in visited:
              visited[(i,jj)] = (dis+jj-j, s2)
            elif visited[(i,jj)] == dis+jj-j: visited[(i,jj)] = (dis+jj-j, min(s2, visited[(i,jj)][1]))
            jj += 1
          jj -= 1
          if jj>j and visited[(i,jj)]==(dis+jj-j,s2): new.append((i,jj))
      last, new = new, []
      cnt += 1
      # break
    if hole in visited: return visited[hole][1]
    else: return 'impossible'


if __name__ == '__main__':
  a = Solution()
  maze = [[0, 0, 0, 0, 0],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0],[0, 1, 0, 0, 1],[0, 1, 0, 0, 0]] 
  print a.findShortestWay(maze, (4,3), (0,1))
  # print a.findShortestWay(maze, (4,3), (3,0))
