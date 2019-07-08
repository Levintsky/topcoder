'''
32. Longest Valid Parentheses (Hard)

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1: return 1
        cnt = 0
        i = 0
        len_ = 0
        best = 0
        while i < n:
            if s[i] == '(':
                cnt += 1
            else:
                cnt -= 1
                
            if cnt > 0:
                len_ += 1
            elif cnt == 0:
                len_ += 1
                best = max(best, len_)
            else:
                cnt, len_ = 0, 0
            i += 1
        print best
        i = n - 1
        len_ = 0
        cnt = 0
        while i >= 0:
            if s[i] == ')': cnt += 1
            else: cnt -= 1
            if cnt > 0: len_ += 1
            elif cnt == 0:
                len_ += 1
                best = max(best, len_)
            else:
                cnt, len_ = 0, 0
            i -= 1
        return best


if __name__ == "__main__":
  a = Solution()
  print a.longestValidParentheses(")()())")
  print a.longestValidParentheses("(((((()")
  print a.longestValidParentheses("()(()")
