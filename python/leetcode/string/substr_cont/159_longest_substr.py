"""
159. Longest Substring with At Most Two Distinct Characters (Hard)

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = "eceba",

T is "ece" which its length is 3.
"""

class Solution(object):
  def lengthOfLongestSubstringTwoDistinct(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    if n <= 2: return n
    rec = {s[0]: 1}

    i = 1
    begin = 0
    best = 1
    while i < n:
      c = s[i]
      # case 1: already in
      if c in rec:
        rec[c] += 1
      else: # already has two
        rec[c] = 1

      while len(rec.keys()) >= 3:
        c = s[begin]
        rec[c] -= 1
        if rec[c] == 0: del rec[c]
        begin += 1
      print(begin, i, s[begin:i+1])
      best = max(best, i-begin+1)
      i += 1
    return best

if __name__ == "__main__":
  a = Solution()
  print(a.lengthOfLongestSubstringTwoDistinct("eceba"))
