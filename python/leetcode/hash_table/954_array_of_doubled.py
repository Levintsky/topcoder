"""
954. Array of Doubled Pairs (Hard)

Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false
 

Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000
"""

import collections


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort(key=lambda item:abs(item))
        c = dict(collections.Counter(A))
        cnt = 0
        n = len(A)
        for item in A:
            if c[item] > 0 and 2 * item not in c.keys():
                return False
            if c[item] > 0:
                c[item] -= 1
                c[2*item] -= 1
        for k in c:
            if c[k] != 0:
                return False
        return True

    def canReorderDoubled(self, A):
        c = collections.Counter(A)
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True

                    
if __name__ == "__main__":
    a = Solution()
    print(a.canReorderDoubled([3,1,3,6]))
    print(a.canReorderDoubled([2,1,2,6]))
    print(a.canReorderDoubled([4,-2,2,-4]))
    print(a.canReorderDoubled([1,2,4,16,8,4]))
    print(a.canReorderDoubled([1,2,4,8]))
