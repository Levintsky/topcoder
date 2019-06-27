"""
949. Largest Time for Given Digits (Easy)

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""

Note:

A.length == 4
0 <= A[i] <= 9
"""

import itertools


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        # step 0: generate all permutation
        Aaug = [item for item in A]
        result_set = set()

        def permute(i):
            if i == 3:
                h = Aaug[0] * 10 + Aaug[1]
                m = Aaug[2] * 10 + Aaug[3]
                if h < 24 and m < 60:
                    result_set.add((h, m))
                return
            for j in range(i, 4):
                Aaug[i], Aaug[j] = Aaug[j], Aaug[i]
                permute(i + 1)
                Aaug[i], Aaug[j] = Aaug[j], Aaug[i]

        permute(0)
        result_set = list(result_set)
        result_set.sort()
        if len(result_set) == 0:
            return ""
        result = result_set[-1]
        result = [str(result[0]), str(result[1])]
        if len(result[0]) == 1:
            result[0] = "0" + result[0]
        if len(result[1]) == 1:
            result[1] = "0" + result[1]
        result = ":".join(result)
        return result

    def solve2(self, A):
        for t in itertools.permutations(A):
            print(t)


if __name__ == "__main__":
    a = Solution()
    print(a.largestTimeFromDigits([1, 2, 3, 4]))
    # print(a.largestTimeFromDigits([5,5,5,5]))
    print(a.solve2([1, 2, 3, 4]))
