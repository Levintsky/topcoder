"""
1020. Partition Array Into Three Parts With Equal Sum (Easy)

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Note:

3 <= A.length <= 50000
-10000 <= A[i] <= 10000
"""


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sum_ = sum(A)
        len_ = len(A)
        if sum_ % 3 != 0:
            return False

        # step 1: check first number
        target = sum_ // 3

        def check(start, end):
            curr = A[start]
            i = start + 1
            while curr != target and i <= end:
                curr = curr + A[i]
                i += 1
            if curr == target:
                return i - 1
            else:
                return -1

        id1 = check(0, len_ - 3)
        if id1 == -1:
            return False
        id2 = check(id1 + 1, len_ - 2)
        if id2 == -1:
            return False
        else:
            return True


if __name__ == "__main__":
    a = Solution()
    print(a.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
    print(a.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
    print(a.canThreePartsEqualSum([6, 3, 3, 5, -2, 2, 5, 1, -9, 4]))
