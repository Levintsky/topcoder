"""
1253. Reconstruct a 2-Row Binary Matrix (Medium)

Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum is given as an integer array with length n.
Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.

Example 1:

Input: upper = 2, lower = 1, colsum = [1,1,1]
Output: [[1,1,0],[0,0,1]]
Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
Example 2:

Input: upper = 2, lower = 3, colsum = [2,2,1,1]
Output: []
Example 3:

Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 

Constraints:

1 <= colsum.length <= 10^5
0 <= upper, lower <= colsum.length
0 <= colsum[i] <= 2
"""

import collections


class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        if sum(colsum) != upper + lower:
        	return []
        c = collections.Counter(colsum)
        if c[2] > upper or c[2] > lower:
        	return []
        upper -= c[2]
        lower -= c[2]
        result = []
        n = len(colsum)
        for i in range(2):
        	result.append([0] * n)
        for i, item in enumerate(colsum):
        	if item == 2:
        		result[0][i] = 1
        		result[1][i] = 1
        	elif item == 1:
        		if upper > 0:
        			result[0][i] = 1
        			upper -= 1
        		else:
        			result[1][i] = 1

        return result

if __name__ == "__main__":
	a = Solution()
	print(a.reconstructMatrix(2, 1, [1,1,1]))
	print(a.reconstructMatrix(2, 3, [2,2,1,1]))
	print(a.reconstructMatrix(5, 5, [2,1,2,0,1,0,1,2,0,1]))
