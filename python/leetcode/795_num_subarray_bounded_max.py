"""
795. Number of Subarrays with Bounded Maximum (Medium)

We are given an array A of positive integers, and two positive integers 
L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the 
value of the maximum array element in that subarray is at least L and at most R.

Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: 
[2], [2, 1], [3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].
"""

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        j = 0
        count = 0
        res = 0
        for i, item in enumerate(A):
            if item >= L and item <= R:
                res += i - j + 1 # all valid since last invalid
                count = i - j + 1
            elif A[i] < L:
                res += count # very smart!
            else:
                j = i + 1
                count = 0
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.numSubarrayBoundedMax([1,2,0], 2, 3))
