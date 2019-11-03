"""
1249. Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        def tackle(ss, op1, op2):
            stat = 0
            res = ""
            for c in ss:
                if c not in [op1, op2]:
                    res += c
                elif c == op1:
                    res += c
                    stat += 1
                else: # )
                    if stat > 0:
                        res += c
                        stat -= 1
            return res

        res1 = tackle(s, '(', ')')
        res1 = res1[::-1]
        res2 = tackle(res1, ')', '(')
        res2 = res2[::-1]
        return res2


if __name__ == "__main__":
    a = Solution()
    print(a.minRemoveToMakeValid("lee(t(c)o)de)"))
    print(a.minRemoveToMakeValid("a)b(c)d"))
    print(a.minRemoveToMakeValid("))(("))
    print(a.minRemoveToMakeValid("(a(b(c)d)"))
