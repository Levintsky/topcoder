"""
859. Buddy Strings (Easy)

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # edge case
        if len(A) != len(B): return False

        def cnt(s):
            result = [0] * 26
            for c in s:
                result[ord(c)-ord('a')] += 1
            return result

        if A == B:
            # any repeating char
            result = cnt(A)
            return max(result) > 1

        idx = []
        for i in range(len(A)):
            if A[i] != B[i]: idx.append(i)
        if len(idx) != 2: return False
        i1, i2 = idx[0], idx[1]
        return A[i1] == B[i2] and B[i1] == A[i2]


if __name__ == "__main__":
    a = Solution()
    print(a.buddyStrings("ab", "ba"))
    print(a.buddyStrings("ab", "ab"))
    print(a.buddyStrings("aa", "aa"))
    print(a.buddyStrings("aaaaaaabc", "aaaaaaacb"))
