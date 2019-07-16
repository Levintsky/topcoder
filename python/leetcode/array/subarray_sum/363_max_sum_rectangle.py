"""
363. Max Sum of Rectangle No Larger Than K (Hard)

Given a non-empty 2D matrix matrix and an integer k, find the max 
sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and
 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""

"""
Solution:

Here's the easily understanding video link for the problem "find the 
max sum rectangle in 2D array": Maximum Sum Rectangular Submatrix in 
Matrix dynamic programming/2D kadane

Notice the key logic:
1. if a subarray starting from index 0 has (cum-sum <= k), update the largest one
2. otherwise, keep it sorted O(nlogn)

slist, num = [], 0
for i in range(row):
    num += sums[i]
    if num <= k: ans = max(ans, num)
    i = bisect.bisect_left(slist, num-k)
    if i != len(slist):
        ans = max(ans, num-slist[i])
    bisect.insort(slist, num)
"""

import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        row = len(matrix)
        if row == 0: return 0
        col = len(matrix[0])
        if col == 0: return 0
        ans = -float("inf")
        for l in range(col): # left
            sums = [0] * row
            for r in range(l, col): # right
                # New intermediate sum
                # for i in range(row):
                sums = [sums[i]+matrix[i][r] for i in range(row)]
                # Variation of 1d kadane, find subarray <= K
                slist, num = [], 0
                for i in range(row):
                    num += sums[i]
                    if num <= k: ans = max(ans, num)
                    i = bisect.bisect_left(slist, num-k)
                    if i != len(slist):
                        ans = max(ans, num-slist[i])
                    bisect.insort(slist, num)
        return ans or 0

    def solve2(self, matrix, k):
        def maxSumSublist(vals):
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for val in vals:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += val
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum
        
        maxSum = float('-inf')
        columns = zip(*matrix)
        for left in range(len(columns)):
            rowSums = [0] * len(matrix)
            for column in columns[left:]:
                rowSums = map(int.__add__, rowSums, column)
                maxSum = max(maxSum, maxSumSublist(rowSums))
        return maxSum


if __name__ == "__main__":
    a = Solution()
    print(a.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))
    # print(a.solve2([[1,0,1],[0,-2,3]], 2))