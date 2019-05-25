"""
741. Cherry Pickup (Hard)

In a N x N grid representing a field of cherries, each cell is one 
of three possible integers. 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and 
pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by 
following the rules below: 

Starting at the position (0, 0) and reaching (N-1, N-1) by 
moving right or down through valid path cells (cells with 
value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left 
or up through valid path cells;
When passing through a path cell containing a cherry, you 
pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then 
no cherries can be collected.

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, 
right right to reach (2, 2).
4 cherries were picked up during this single trip, 
and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return 
home, picking up one more cherry.
The total number of cherries picked up is 5, and 
this is the maximum possible. 

Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not 
-1.
"""

"""
Solution: DP
starting from (0, 0), len(grid)=n
2 * (n-1) steps needed to go from (0, 0) to the right corner

dp[i][j][k]:
for two paths, one ends at (i, k-i), the other ends at (j, k-j)

thorn: -1

dp[i][k] = max(dp[i-1][k-1], dp[i][k-1])
dp[j][k] = max(dp[j-1][k-1], dp[j][k-1])
if [i][k-i] has a cherry: += 1
if [j][k-j] has a cherry: += 1
if i==j and has a cherry: -=1
"""


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        curr = [[-1] * n for _ in range(n)]

        curr[0][0] = grid[0][0]

        for k in range(1, 2*(n-1)+1): # k-steps
            new = [[-1] * n for _ in range(n)]
            for i in range(min(n, k+1)):
                if k - i >= n: continue
                for j in range(min(n, k+1)):
                    if k -j >= n: continue
                    # if it is thorn, always -1
                    if grid[i][k-i] == -1 or grid[j][k-j] == -1:
                        continue

                    result = curr[i][j]
                    if i > 0:
                        result = max(result, curr[i-1][j])
                    if j > 0:
                        result = max(result, curr[i][j-1])
                    if i > 0 and j > 0:
                        result = max(result, curr[i-1][j-1])

                    # very important!
                    # otherwise the result will be wrong
                    if result < 0: continue

                    result += grid[i][k-i]
                    result += grid[j][k-j]
                    if i == j and grid[i][k-i] == 1:
                        result -= 1
                    new[i][j] = result
            curr = new
        return max(curr[n-1][n-1], 0)


if __name__ == "__main__":
    a = Solution()
    # array = [[0, 1, -1], [1, 0, -1], [1, 1,  1]]
    array = [[1,1,-1],[1,-1,1],[-1,1,1]]
    print(a.cherryPickup(array))