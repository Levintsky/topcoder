"""
648. Replace Words (Medium)

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""

class Trie(object):
  def __init__(self):
    self.mapping = {}
    self.is_word = False


class Solution(object):
  def replaceWords(self, dict, sentence):
    """
    :type dict: List[str]
    :type sentence: str
    :rtype: str
    """
    root = Trie()
    for word in dict:
      # add to the Trie
      node = root
      for i in range(len(word)):
        c = word[i]
        if c not in node.mapping:
          node.mapping[c] = Trie()
        node = node.mapping[c]
        if i == len(word)-1:
          node.is_word = True

    result = []
    sentence_list = sentence.split(" ")
    for word in sentence_list:
      # check the word in Trie()
      # if has a prefix in Trie(), return prefix
      # if not found, return itself
      node = root
      tmp = ""
      found = False
      for c in word:
        if node.is_word:
          found = True
          break
        if c not in node.mapping:
          break
        tmp = tmp+c
        node = node.mapping[c]
      if found:
        result.append(tmp)
      else:
        result.append(word)

    # print result
    return " ".join(result)


if __name__ == '__main__':
  a = Solution()
  print a.replaceWords(["cat", "bat", "rat", "catt"], "the cattle was rattled by the battery")
