"""
5. Longest Palindromic Substring (Medium)

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return 0
        res = s[0]

        def check_long(s, i, j):
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    i, j = i-1, j+1
                else:
                    break
            i, j = i+1, j-1
            return j-i+1
        # odd
        for i in range(n):
            len_ = check_long(s, i, i)
            if len_ > len(res):
                # print(i, len_, i-len_//2, i+len_//2)
                res = s[i-len_//2:i+len_//2+1]
        # even
        for i in range(n-1):
            if s[i] == s[i+1]:
                len_ = check_long(s, i, i+1)
                if len_ > len(res):
                    res = s[i-len_//2+1:i+len_//2+1]
                # res = max(res, check_long(s, i, i+1))
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.longestPalindrome("babad"))
    print(a.longestPalindrome("cbbd"))