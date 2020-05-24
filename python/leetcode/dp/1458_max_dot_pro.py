"""
1458. Max Dot Product of Two Subsequences (Hard)

Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.
 

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
"""

class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        memo = {} # (i, j)
        n1, n2 = len(nums1), len(nums2)
        # init:
        # min1, max1 = float('inf'), -float('inf')
        # min2, max2 = float('inf'), -float('inf')
        for i in range(n1-1, -1, -1):
            # min1 = min(min1, nums1[i])
            # max1 = max(max1, nums1[i])
            # print(i, min1, max1)

            for j in range(n2-1, -1, -1):
                # min2 = min(min2, nums2[j])
                # max2 = min(min2, nums2[j])
                if (i, j) not in memo:
                    memo[i, j] = nums1[i] * nums2[j]
                if (i+1, j) in memo:
                    memo[i, j] = max(memo[i,j], memo[i+1, j])
                if (i, j+1) in memo:
                    memo[i, j] = max(memo[i,j], memo[i, j+1])

                # best = max(min1*min2, min1*max2, max1*min2, max1*max2)
                # memo[i, j] = best
        # print(memo)

        for k in range(1, min(n1, n2)+1):
            new_memo = {}
            for i in range(n1-1, -1, -1):
                for j in range(n2-1, -1, -1):
                    new_memo[i, j] = memo[i, j]
                    if (i+1, j+1) in new_memo:
                        new_memo[i, j] = max(memo[i+1, j+1]+nums1[i]*nums2[j], new_memo[i,j])
                    if (i+1, j) in new_memo:
                        new_memo[i, j] = max(new_memo[i+1, j], new_memo[i, j])
                    if (i, j+1) in new_memo:
                        new_memo[i, j] = max(new_memo[i, j+1], new_memo[i, j])
            memo = new_memo
        return memo[0, 0]

    def solve2(self, nums1, nums2):
        n1, n2 = len(nums1), len(nums2)
        result = []
        for i in range(n1):
            result.append([-float('inf')] * n2)
        for i in range(n1):
            for j in range(n2):
                result[i][j] = max(nums1[i] * nums2[j], result[i][j])
                if i > 0 and j > 0:
                    result[i][j] = max(result[i][j], nums1[i] * nums2[j] + result[i-1][j-1])
                if i > 0:
                    result[i][j] = max(result[i][j], result[i-1][j])
                if j > 0:
                    result[i][j] = max(result[i][j], result[i][j-1])
        return result[n1-1][n2-1]


if __name__ == "__main__":
    a = Solution()
    # print(a.maxDotProduct([2,1,-2,5], [3,0,-6]))
    print(a.solve2([2,1,-2,5], [3,0,-6]))
    # print(a.maxDotProduct([3,-2], [2,-6,7]))
    print(a.solve2([3,-2], [2,-6,7]))
    # print(a.maxDotProduct([-1,-1], [1,1]))
    print(a.solve2([-1,-1], [1,1]))
