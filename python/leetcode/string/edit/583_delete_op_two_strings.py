'''
583. Delete Operation for Two Strings (DP)

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
'''

class Solution(object):
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    n1 = len(word1)
    n2 = len(word2)
    result = []
    for i in range(n1+1): result.append([0]*(n2+1))
    # result[i1][[i2] longest subseq of word[0:i1] word2[0:i2]
    
    for i1 in range(1, n1+1):
      for i2 in range(1, n2+1):
        if word1[i1-1] == word2[i2-1]: result[i1][i2] = result[i1-1][i2-1] + 1
        else: result[i1][i2] = max(result[i1-1][i2], result[i1][i2-1])
    return n1+n2-2*result[-1][-1]

if __name__ == '__main__':
  a = Solution()
  print a.minDistance('sea', 'eat')
  print a.minDistance('', 'b')
     
