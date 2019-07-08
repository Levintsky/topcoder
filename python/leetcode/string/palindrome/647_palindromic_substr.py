"""
647. Palindromic Substrings (Medium)

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""

class Solution(object):
  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    n = len(s)
    print 'odd'
    for i in range(n):
      x = self.helper_odd(s, i)
      print i, x
      result += (x+1)/2
    print 'even'
    for i in range(n-1):
      x = self.helper_even(s, i)
      print i, x
      result += x/2
    return result
   
  def helper_odd(self, s, i):
    # longest palin centered at i
    n = len(s)
    j = 0
    while i-j>=0 and i+j<n:
      if s[i-j] == s[i+j]:
        j += 1
      else:
        break
    j -= 1
    return j*2+1

  def helper_even(self, s, i):
    # longest palin centered at (i,i+1)
    n = len(s)
    if i+1>=n or s[i] != s[i+1]:
      return 0
    begin, end = i, i+1
    while begin>=0 and end<n:
      if s[begin] == s[end]:
        begin -= 1
        end += 1
      else:
        break
    begin += 1
    end -= 1
    return end-begin+1

if __name__ == "__main__":
  a = Solution()
  print a.countSubstrings("baaab")
