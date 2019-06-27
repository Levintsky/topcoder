"""
1021. Best Sightseeing Pair (Medium)

Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

Note:

2 <= A.length <= 50000
1 <= A[i] <= 1000
"""


class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        best1 = max(A[0] - 1, A[1])
        best2 = A[0] + A[1] - 1

        for item in A[2:]:
            # update best2:
            best2 = max(best2, best1 - 1 + item)
            best1 = max(best1 - 1, item)
        return best2


if __name__ == "__main__":
    a = Solution()
    print(a.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
