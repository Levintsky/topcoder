"""
524. Longest Word in Dictionary through Deleting (Medium)

Given a string and a string dictionary, find the longest string in the dictionary that 
can be formed by deleting some characters of the given string. If there are more than 
one possible results, return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""

class Solution(object):
  def findLongestWord(self, s, d):
    """
    :type s: str
    :type d: List[str]
    :rtype: str
    """
    d.sort(key= lambda k: (-len(k), k))
    for i in range(len(d)):
      if self.is_sub(s, d[i]):
        return d[i]
    return ''

  def is_sub(self, a, b):
    i = 0
    j = 0
    na = len(a)
    nb = len(b)
    if na<nb: return False
    while i<na and j<nb:
      if a[i] == b[j]:
        i += 1
        j += 1
      else:
        i += 1
    return j==nb

if __name__ == '__main__':
  a = Solution()
  print a.findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"])
  print a.findLongestWord(s = "abpcplea", d = ["a","b","c"])

