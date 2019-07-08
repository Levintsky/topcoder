'''
522. Longest Uncommon Subsequence II (Medium)

Given a list of strings, you need to find the longest uncommon subsequence among them. 
The longest uncommon subsequence is defined as the longest subsequence of one of these 
strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some 
characters without changing the order of the remaining elements. Trivially, any string 
is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the 
longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, 
return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3

Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
'''

class Solution(object):
  def findLUSlength(self, strs):
    """
    :type strs: List[str]
    :rtype: int
    """
    strs.sort(key=len, reverse=True)
    # arrange strs
    # tmp_str = strs[0]
    for i in range(0, len(strs)):
      str1 = strs[i]
      flag = True
      for j in range(0, len(strs)):
        if j == i: continue
        if self.is_sub(strs[i], strs[j]):
            flag = False
            break
      if flag: return len(strs[i])
    return -1

  def is_sub(self, str1, str2):
    # return if str1 is a subseq of str2
    i1 = 0
    i2 = 0
    while(i1<len(str1) and i2<len(str2)):
      if str1[i1] == str2[i2]:
        i1, i2 = i1+1, i2+1
      else:
        i2 += 1
    return i1==len(str1)


if __name__ == '__main__':
  a = Solution()
  print a.findLUSlength(["aba", "cdc", "eae"])
  print a.findLUSlength(["aaa", "aaa", "aa"])
  print a.findLUSlength(["aabbcc", "aabbcc","bc","bcc","aabbccc"])
  print a.findLUSlength(["a","b","c","d","e","f","a","b","c","d","e","f"])
