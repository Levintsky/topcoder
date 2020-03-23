"""
1391. Check if There is a Valid Path in a Grid
Medium

57

71

Add to List

Share
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""

class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        visited.add((0, 0))

        if m == 1 and n == 1:
            return True
        
        def visit(curr, last):
            cnt = 1
            while True:
                # visit next
                i, j = curr
                if grid[i][j] == 1:
                    cand = [(i, j-1), (i, j+1)]
                elif grid[i][j] == 2:
                    cand = [(i-1, j), (i+1, j)]
                elif grid[i][j] == 3:
                    cand = [(i, j-1), (i+1, j)]
                elif grid[i][j] == 4:
                    cand = [(i, j+1), (i+1, j)]
                elif grid[i][j] == 5:
                    cand = [(i, j-1), (i-1, j)]
                elif grid[i][j] == 6:
                    cand = [(i-1, j), (i, j+1)]

                if cand[0] == last:
                    last = curr
                    curr = cand[1]
                elif cand[1] == last:
                    last = curr
                    curr = cand[0]
                else: # doesn't connect last
                    return False

                if last == (m-1, n-1):
                    return True

                if curr[0] in [-1, m] or curr[1] in [-1, n] or curr in visited:
                    return False
                else:
                    visited.add(curr)
                    # cnt += 1
            # return cnt

        curr = 0, 0
        if grid[0][0] in [1, 3]:
            last = 0, -1
            return visit(curr, last)
        elif grid[0][0] in [2, 6]:
            last = -1, 0
            return visit(curr, last)
        elif grid[0][0] == 4:
            return visit(curr, (1, 0)) or visit(curr, (0, 1))
        elif grid[0][0] == 5:
            return visit(curr, (-1, 0)) or visit(curr, (0, -1))
        
        """
        if last[0] == m-1 and last[1] == n-1 and cnt == m*n:
            return True
        else:
            return False
        """


if __name__ == "__main__":
    a = Solution()
    assert a.hasValidPath([[2,4,3],[6,5,2]])
    assert not a.hasValidPath([[1,2,1],[1,2,1]])
    assert not a.hasValidPath([[1,1,2]])
    assert a.hasValidPath([[1,1,1,1,1,1,3]])
    assert a.hasValidPath([[4,1],[6,1]])
    assert a.hasValidPath([[2],[2],[2],[2],[2],[2],[6]])
    assert a.hasValidPath([[4,3],[6,5]])
