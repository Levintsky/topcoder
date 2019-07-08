"""
340. Longest Substring with At Most K Distinct Characters (Hard)

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = "eceba" and k = 2,

T is "ece" which its length is 3.
"""

class Solution(object):
  def lengthOfLongestSubstringKDistinct(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    result = 0
    rec = {}
    n = len(s)
    if n == 0: return 0
    if k == 0: return 0

    # init
    c = s[0]
    rec[c] = 1
    result = 1
    l = 0

    for i in range(1, n):
      c = s[i]
      rec[c] = rec.get(c, 0) + 1
      print i, c, rec,
      if len(rec.keys()) <= k:
        result = max(result, i-l+1)
      else:
        while len(rec) > k:
          c = s[l]
          l += 1
          rec[c] -= 1
          if rec[c] == 0: del rec[c]
      print rec, l
    return result


if __name__ == "__main__":
  a = Solution()
  print a.lengthOfLongestSubstringKDistinct("eceba", 2)
