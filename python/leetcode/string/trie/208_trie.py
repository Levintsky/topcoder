'''
208. Implement Trie (Prefix Tree) (Medium)

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode():
  def __init__(self):
    self.child = {} # char to other TrieNode
    self.is_end = False


class Trie(object):
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    node = self.root
    for c in word:
      if c not in node.child:
        node.child[c] = TrieNode()
      node = node.child[c]
    node.is_end = True

  def search(self, word):
    node = self.root
    for c in word:
      if c not in node.child:
        return False
      else:
        node = node.child[c]
    return node.is_end
    
  def startsWith(self, prefix):
    node = self.root
    for c in prefix:
      if c not in node.child:
        return False
      else:
        node = node.child[c]
    return True


if __name__ == '__main__':
  trie = Trie()
  trie.insert('ab')
  print trie.search('a')
  print trie.search('ab')
  print trie.startsWith('a')
  print trie.startsWith('ab')
