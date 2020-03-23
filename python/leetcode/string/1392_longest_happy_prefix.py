"""
1392. Longest Happy Prefix (Hard)

A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
Example 3:

Input: s = "leetcodeleet"
Output: "leet"
Example 4:

Input: s = "a"
Output: ""

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
"""

class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, l, r, mod = 0, 0, 0, 10**9 + 7
        for i in xrange(len(s) - 1):
            l = (l * 128 + ord(s[i])) % mod
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod
            if l == r: res = i + 1
        return s[:res]