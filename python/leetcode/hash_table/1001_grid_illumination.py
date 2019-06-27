"""
1001. Grid Illumination (Hard)

On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

Example 1:

Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation:
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.

Note:

1 <= N <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == queries[i].length == 2
"""

"""
Solution:
4 hash table:
row[i]: how many lights are on in row[i]
col[i]: how many lights are on in col[i]
diag1[i]: how many lights are on in diag1[i]
diag2[i]: how many lights are on in diag2[i]
1 extra set:
all on lights (x, y)
"""


class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        row = {}
        col = {}
        diag1 = {}
        diag2 = {}
        light_set = set()

        # step 1: preprocessing
        for i, j in lamps:
            if (i, j) not in light_set:
                light_set.add((i, j))
                row[i] = row.get(i, 0) + 1
                col[j] = col.get(j, 0) + 1
                diag1[j - i + N - 1] = diag1.get(j - i + N - 1, 0) + 1
                diag2[j + i] = diag2.get(j + i, 0) + 1
        print(row, col, diag1, diag2)

        result = []
        for i, j in queries:
            tmp = 0
            if i in row:
                tmp = 1
            if j in col:
                tmp = 1
            if j - i + N - 1 in diag1:
                tmp = 1
            if j + i in diag2:
                tmp = 1
            result.append(tmp)
            for ii in range(max(0, i - 1), min(i + 2, N)):
                for jj in range(max(0, j - 1), min(j + 2, N)):
                    if (ii, jj) in light_set:
                        light_set.remove((ii, jj))
                        row[ii] -= 1
                        col[jj] -= 1
                        diag1[jj - ii + N - 1] -= 1
                        diag2[jj + ii] -= 1
                        if row[ii] == 0:
                            del row[ii]
                        if col[jj] == 0:
                            del col[jj]
                        if diag1[jj - ii + N - 1] == 0:
                            del diag1[jj - ii + N - 1]
                        if diag2[jj + ii] == 0:
                            del diag2[jj + ii]
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 0]]))
