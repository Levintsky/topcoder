"""
1072. Flip Columns For Maximum Number of Equal Rows (Medium)

Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

Note:

1 <= matrix.length <= 300
1 <= matrix[i].length <= 300
All matrix[i].length's are equal
matrix[i][j] is 0 or 1
"""

import collections

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        init = [item[0] for item in matrix] # m-dim

        def dfs(ii, curr):
            if ii == n:
                res = 0
                for i in range(m):
                    if curr[i] is not None:
                        res += 1
                return res
            if curr == [None] * m:
                return 0

            tmp = [item[ii] for item in matrix]
            result = [item for item in curr]
            for i in range(m):
                if tmp[i] != curr[i]:
                    result[i] = None
            f1 = dfs(ii+1, result)

            tmp = [1-item[ii] for item in matrix]
            result = [item for item in curr]
            for i in range(m):
                if tmp[i] != curr[i]:
                    result[i] = None
            f2 = dfs(ii+1, result)
            return max(f1, f2)
        result = dfs(1, init)
        return result

    def solve2(self, A):
        results = []
        for r in A:
            tmp = [x ^ r[0] for x in r]
            results.append(tuple(tmp))
        # results = [tuple(x ^ r[0] for x in r) for r in A]
        memo = collections.Counter(results)
        return max(memo.values())

if __name__ == "__main__":
    a = Solution()
    # print(a.maxEqualRowsAfterFlips([[0,1],[1,1]]))
    print(a.solve2([[0,1],[1,0]]))
