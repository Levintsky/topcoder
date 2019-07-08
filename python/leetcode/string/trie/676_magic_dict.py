"""
676. Implement Magic Dictionary (Medium)

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""

class TrieNode(object):
  def __init__(self):
    self.is_word = False
    self.mapping = {}
    self.word = None

class MagicDic(object):
  def __init__(self):
    self.root = TrieNode()

  def buildDict(self, dict):
    for word in dict:
      node = self.root
      for i in range(len(word)):
        c = word[i]
        if c not in node.mapping:
          node.mapping[c] = TrieNode()
        node = node.mapping[c]
        if i == len(word) - 1:
          node.is_word = True
          node.word = word

  def search(self, word):
    if word == "": return False
    n = len(word)
    for i in range(n):
      tmp_word = word[:i] + '*' + word[i+1:]
      # tmp_word[i] = '*'
      print tmp_word

      # search tmp_word in the trie
      self.result = set()
      node = self.root
      self.helper(node, tmp_word, 0)
      print self.result
      for item in self.result:
        if item[i] != word[i]: return True
    return False

  def helper(self, node, word_, i):
    if i == len(word_):
      if node.is_word:
        self.result.add(node.word)
      return

    c = word_[i]
    print c, node, type(c), type(node)
    if c != '*':
      if c in node.mapping:
        self.helper(node.mapping[c], word_, i+1)
      else:
        return
    else:
      for cc in node.mapping:
        self.helper(node.mapping[cc], word_, i+1)


if __name__ == "__main__":
  a = MagicDic()
  a.buildDict(["hello", "leetcode"])

  # print a.search('hello')
  # print a.search('hhllo')
  # print a.search('hell')
  print a.search('leetcoded')
