"""
696. Count Binary Substrings (Easy)

Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: 
"0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""

class Solution(object):
  def countBinarySubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = []
    n = len(s)
    for i in range(n):
      c = s[i]
      if i == 0 or c != s[i-1]:
        res.append(1)
      else:
        res[-1] += 1
    print res

    ret = 0
    n = len(res)
    for i in range(n-1):
      ret += min(res[i], res[i+1])
    return ret


if __name__ == "__main__":
  a = Solution()
  print a.countBinarySubstrings("00110011")
  print a.countBinarySubstrings("10101")
