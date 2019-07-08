"""
10. Regular Expression Matching (Hard)

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.helper(s, p, 0, 0)

    def helper(self, s, p, i, j):
        ls = len(s)
        lp = len(p)
        # boundary condition: end
        if i == ls:
            while j < lp - 1 and p[j + 1] == "*":
                j += 2
            return j == lp
        if j == lp:
            return i == ls
        # case 1:
        # print s[i], p[j]

        if j < lp - 1 and p[j + 1] == "*":
            c = p[j]  # char
            j += 2
            while j < lp - 1 and p[j] == c and p[j + 1] == "*":
                j += 2
            i_start = i
            if c != ".":
                while i < ls and s[i] == c:
                    i += 1
            else:
                i = ls
            ii = i
            # print ii, j, c
            while ii >= i_start:
                if self.helper(s, p, ii, j):
                    return True
                ii -= 1
            return False
        elif p[j] == "." or s[i] == p[j]:
            return self.helper(s, p, i + 1, j + 1)
        else:
            return False
