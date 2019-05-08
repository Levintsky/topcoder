"""
1039. Minimum Score Triangulation of Polygon (Medium)

Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:
Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.

Example 3:

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

Note:

3 <= A.length <= 50
1 <= A[i] <= 100
"""

"""
Python, bottom-up

    def minScoreTriangulation(self, A):
        n = len(A)
        dp = [[0] * n for i in xrange(n)]
        for d in xrange(2, n):
            for i in xrange(n - d):
                j = i + d
                dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[j] * A[k] for k in xrange(i + 1, j))
        return dp[0][n - 1]
Python, top-down:

    def minScoreTriangulation(self, A):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
            return memo[i, j]
        return dp(0, len(A) - 1)
"""

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.memo = {}

        def dp(list_):
        	# base cases:
        	if len(list_) < 3:
        		self.memo[tuple(list_)] = 0
        		return 0
        	# check if appeared?
        	for i in range(len(list_)):
        		tmplist = list_[i:] + list_[:i]
        		if tuple(tmplist) in self.memo:
        			return self.memo[tuple(tmplist)]
        	if len(list_) == 3:
        		self.memo[tuple(list_)] = list_[0] * list_[1] * list_[2]
        		return self.memo[tuple(list_)]
        	min_result = dp([list_[-1], list_[0], list_[1]])
        	min_result += dp(list_[1:])
        	for i in range(2, len(list_)-1):
        		curr_result = dp(list_[:i+1])
        		curr_result += dp(list_[i:] + [list_[0]])
        		min_result = min(min_result, curr_result)
        	self.memo[tuple(list_)] = min_result
        	return min_result
        result = dp(A)
        print(self.memo)
        return result

    def solve2(self, A):
        n = len(A)
        full_result = []
        result = []
        for i in range(n-2):
            result.append(A[i]*A[i+1]*A[i+2])
        full_result.append(result)

        for i in range(1, n-2): #
            new_result = []
            # full_result[0]: 3 points, 0..2, 1..3, j..j+2
            # full_result[1]: 4 points, 0..3, 1..4, j..j+3
            #  ...
            # full_result[i]: 3+i points, 0..2+i, 1..3+i
            for j in range(n-i-2):
    		    # starting point

    			# new_result[j]: j..2+i+j
    			# new3: j..k, k..2+i+j, (j, k, 2+i+j)
                min_result = None
                for k in range(j+1, 2+i+j):
                    if k-j > 1: tmp1 = full_result[k-j-2][j]
                    else: tmp1 = 0
                    # print(j,k,3+i+j,"||",A[j], A[k], A[3+i+j])
                    tmp2 = A[j] * A[k] * A[2+i+j]
                    if i+j-k >= 0: tmp3 = full_result[i+j-k][k]
                    else: tmp3 = 0
                    if min_result is None: min_result = tmp1+tmp2+tmp3
                    else: min_result = min(min_result, tmp1+tmp2+tmp3)
                new_result.append(min_result)
            full_result.append(new_result)
        return full_result[-1][0]

if __name__ == "__main__":
	a = Solution()
	# print(a.minScoreTriangulation([1,2,3]))
	print(a.solve2([1,2,3]))
	# print(a.minScoreTriangulation([3,7,4,5]))
	print(a.solve2([3,7,4,5]))
	# print(a.minScoreTriangulation([1,3,1,4,1,5]))
	print(a.solve2([1,3,1,4,1,5]))
