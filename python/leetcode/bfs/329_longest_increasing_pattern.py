'''
329. Longest Increasing Path in a Matrix (Hard)

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

class Solution(object):
  def longestIncreasingPath(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    m = len(matrix)
    if m == 0: return 0
    n = len(matrix[0])
    if n == 0: return 0
    self.result = []
    self.visited = []
    for i in range(m):
      self.result.append([1]*n)
      self.visited.append([False]*n)

    for i in range(m):
      for j in range(n):
        self.dfs(matrix, i, j)
    # self.dfs(matrix, 0, 0)
    # print self.result
    # print self.visited
    result = max([max(item) for item in self.result])
    return result

  def dfs(self, matrix, i, j):
    print i,j
    m = len(matrix)
    n = len(matrix[0])
    tmp_len = 1
    # search up
    if i>0 and matrix[i-1][j]>matrix[i][j]:
      if not self.visited[i-1][j]:
        self.dfs(matrix,i-1,j)
      tmp_len = max(tmp_len, 1+self.result[i-1][j])
    # search down
    if i<m-1 and matrix[i+1][j]>matrix[i][j]:
      if not self.visited[i+1][j]:
        self.dfs(matrix,i+1,j)
      tmp_len = max(tmp_len, 1+self.result[i+1][j])
    # search left
    if j>0 and matrix[i][j-1]>matrix[i][j]:
      if not self.visited[i][j-1]:
        self.dfs(matrix,i,j-1)
      tmp_len = max(tmp_len, 1+self.result[i][j-1])
    # search right
    if j<n-1 and matrix[i][j+1]>matrix[i][j]:
      print 'here'
      if not self.visited[i][j+1]:
        self.dfs(matrix,i,j+1)
      tmp_len = max(tmp_len, 1+self.result[i][j+1])
    self.visited[i][j] = True
    self.result[i][j] = tmp_len

if __name__ == "__main__":
  a = Solution()
  print a.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
  print a.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
