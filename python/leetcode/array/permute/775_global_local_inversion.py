"""
775. Global and Local Inversions (Medium)

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.

Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
"""

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n <= 2:
            return True
        n1, n2 = max(A[0], A[1]), min(A[0], A[1])
        for i in range(2, n):
            if A[i] > n1: # new larger
                n1, n2 = A[i], n1
            elif A[i] > n2 and A[i] < A[i-1]: # local inversion
                n2 = A[i]
            else:
                return False
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isIdealPermutation([1, 0, 2]))
    print(a.isIdealPermutation([1, 2, 0]))
    print(a.isIdealPermutation([1, 3, 2, 4]))
    print(a.isIdealPermutation([2, 0, 1]))
