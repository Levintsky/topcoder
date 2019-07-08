"""
472. Concatenated Words (Hard)

Given a list of words (without duplicates), please write a program that returns all 
concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two 
shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""

"""
dfs: recursive
# trie for look-up
"""

class TrieNode(object):
  def __init__(self):
    self.isword = False
    self.mapping = {}

class Solution(object):
  def findAllConcatenatedWordsInADict(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    self.root = TrieNode()
    # step 0: sort words by length
    words.sort(key=len)

    # step 1: build a trie for look up in words
    result = []
    for word in words:
      if len(word) == 0: continue
      # dfs check
      cnt = self.dfs(word, 0)
      print word, cnt
      if cnt >= 2: result.append(word)

      # add current word to the Trie
      tmp = self.root
      for i in range(len(word)):
        if word[i] not in tmp.mapping:
          tmp_new = TrieNode()
          tmp.mapping[word[i]] = tmp_new
        tmp = tmp.mapping[word[i]]
        if i == len(word) - 1: tmp.isword = True
    return result
    
  def dfs(self, word, i):
    # check if word[i] can be done by two words
    pos = []
    tmp = self.root
    cnt = 0
    for ii in range(i, len(word)):
      if word[ii] in tmp.mapping:
        tmp = tmp.mapping[word[ii]]
        if tmp.isword:
          pos.append(ii+1)
          cnt = 1
      else: break
    # print i, pos
    if len(pos) == 0: return -1
    # go through potential pos
    max_cnt = -1
    for p in pos[::-1]:
      if p < len(word):
        result = self.dfs(word, p)
        if result > 0:
          max_cnt = max(max_cnt, 1+result)
        if max_cnt >=2: return 2
      else:
        max_cnt = max(max_cnt, 1)
      # print 'p', p, 'last pos', len(word)-1, max_cnt
    return max_cnt


if __name__ == '__main__':
  a = Solution()
  print a.findAllConcatenatedWordsInADict(['cat','dog','catdog','cats','catsdog'])
  print a.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
  print a.findAllConcatenatedWordsInADict(['a','b','ab','abc'])
