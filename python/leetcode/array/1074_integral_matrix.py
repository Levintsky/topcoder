"""
1074. Number of Submatrices That Sum to Target (Hard)

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
 

Note:

1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""

"""
Solution:
1. Integral row (integral image) to fast get subarray sum
2. [i1, j1, i2, j2], should be O(n^4),
  with hash table, reduce to O(n^3), only [j1,i2,j2]
  i1 reduced by hash table
"""

import collections


class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        inte = []
        for i in range(m):
            inte.append([0] * n)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    inte[i][j] = matrix[i][j]
                elif i == 0:
                    inte[i][j] = inte[i][j - 1] + matrix[i][j]
                elif j == 0:
                    inte[i][j] = inte[i - 1][j] + matrix[i][j]
                else:
                    inte[i][j] = (
                        inte[i - 1][j]
                        + inte[i][j - 1]
                        - inte[i - 1][j - 1]
                        + matrix[i][j]
                    )

        res = 0
        for i in range(m):
            # memo = {}
            for j in range(n):
                # if inte[i][j] == target:
                #     res += 1
                for ii in range(i + 1):
                    for jj in range(j + 1):
                        if ii == 0 and jj == 0:
                            tmp = inte[i][j]
                        elif ii == 0:
                            tmp = inte[i][j] - inte[i][jj - 1]
                        elif jj == 0:
                            tmp = inte[i][j] - inte[ii - 1][j]
                        else:
                            tmp = (
                                inte[i][j]
                                - inte[ii - 1][j]
                                - inte[i][jj - 1]
                                + inte[ii - 1][jj - 1]
                            )
                        if tmp == target:
                            res += 1
                print(i, j, res)
                """

                    key = inte[ii][j]
                    memo[key] = memo.get(key, 0) + 1
                curr = inte[i][j]
                res += memo.get(curr - target, 0)

                memo[curr] = memo.get(curr, 0) + 1
                """
        return res

    def solve2(self, A, target):
        m, n = len(A), len(A[0])
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = collections.Counter({0: 1})
                cur = 0
                for k in range(m):
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0))
    print(a.solve2([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
