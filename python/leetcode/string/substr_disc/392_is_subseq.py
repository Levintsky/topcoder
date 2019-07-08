"""
392. Is Subsequence (Medium)

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""
# binary search for the follow-up

class Solution(object):
  def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    sn = len(s)
    si = 0 
    tn = len(t)
    ti = 0

    while(si<sn and ti<tn):
      # si, ti match, go forward
      if s[si] == t[ti]:
        si += 1
        ti += 1
      else:
        ti += 1
    if si == sn: return True
    else: return False


if __name__ == '__main__':
  a = Solution()
  print a.isSubsequence('abc', 'ahbgdc')
  print a.isSubsequence('axc', 'ahbgdc')
