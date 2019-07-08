"""
161. One Edit Distance (Medium)

Given two strings S and T, determine if they are both one edit distance apart.
"""

class Solution(object):
  def isOneEditDistance(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    ns = len(s)
    nt = len(t)
    if ns == nt + 1 and self.check1(s, t):
      return True
    if ns + 1 == nt and self.check1(t, s):
      return True
    if ns == nt and self.check2(s, t):
      return True
    return False

  def check1(self, s, t):
    # delete 1 char in s
    ns, nt = len(s), len(t)
    if ns != nt + 1: return False
    i = 0
    while i < nt and s[i] == t[i]:
      i += 1

    return s[i+1:] == t[i:]

  def check2(self, s, t):
    # check 1 update away
    flag = 0
    i = 0
    ns, nt = len(s), len(t)
    if ns != nt: return False

    i = 0
    while i < ns:
      if s[i] != t[i] and flag == 0:
        flag = 1
      elif s[i] != t[i] and flag == 1:
        return False
      i += 1
    return flag == 1


if __name__ == "__main__":
  a = Solution()
  print a.isOneEditDistance("a", "")
