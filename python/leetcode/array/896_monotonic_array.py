"""
896. Monotonic Array (Easy)

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        i = 1
        # check increasing
        while i < n:
            if A[i] < A[i - 1]:
                break
            i += 1
        if i == n:
            return True
        i = 1
        # check decreasing
        while i < n:
            if A[i] > A[i - 1]:
                return False
            i += 1
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isMonotonic([1, 2, 2, 3]))
    print(a.isMonotonic([6, 5, 4, 4]))
    print(a.isMonotonic([1, 3, 2]))
    print(a.isMonotonic([1, 2, 4, 5]))
    print(a.isMonotonic([1, 1, 1]))
