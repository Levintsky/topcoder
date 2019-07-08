'''
567. Permutation in String (Medium)

Given two strings s1 and s2, write a function to return true if s2 contains the 
permutation of s1. In other words, one of the first string's permutations is the 
substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

class Solution(object):
  def checkInclusion(self, s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    # statistics of 's1'
    n1 = len(s1)
    cnt = [0] * 26
    for i in range(n1):
      tmp = ord(s1[i]) - ord('a')
      cnt[tmp] += 1
    # 
    n2 = len(s2)
    # init
    if n2<n1: return False
    cnt2 = [0]*26
    for i in range(n1):
      tmp = ord(s2[i]) - ord('a')
      cnt2[tmp] += 1
    if self.helper(cnt, cnt2): return True
    i = n1
    while i<n2:
      # add s2[i]
      tmp = ord(s2[i]) - ord('a')
      cnt2[tmp] += 1
      # removes2[i-n1]
      tmp = ord(s2[i-n1]) - ord('a')
      cnt2[tmp] -= 1
      # stat
      if self.helper(cnt, cnt2): return True
      i += 1
    return False
  def helper(self, cnt1, cnt2):
    for i in range(26):
      if cnt1[i] != cnt2[i]: return False
    return True


if __name__ == '__main__':
  a = Solution()
  print a.checkInclusion('ab', "eidbaooo")
  print a.checkInclusion('ab', "eidboaoo")
