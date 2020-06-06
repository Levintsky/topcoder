'''
211. Add and Search Word - Data structure design (Medium)

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one 
letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
'''

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len_dic = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        w_len = len(word)
        if w_len > 0:
            if w_len in self.len_dic:
                self.len_dic[w_len].append(word)
            else:
                self.len_dic[w_len] = [word]
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        w_len = len(word)
        if w_len not in self.len_dic:
            return False
        if '.' not in word:
            return word in self.len_dic[w_len]
        for item in self.len_dic[w_len]:
            # compare
            for j in range(w_len):
                if item[j] != word[j] and word[j]!='.':
                    break
                # print j, item, word
            else:
              return True
        return False


# Solution 2: by Trie
class TrieNode():
    def __init__(self):
        self.dic = {}
        self.is_end = False
        
        
class WordDictionary2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.dic:
                node.dic[c] = TrieNode()
            node = node.dic[c]
        node.is_end = True
                

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        self.res = False
        self.dfs(self.root, word)
        return self.res
            
    def dfs(self, node, word):
        if not self.res:
            if not word:
                if node.is_end:
                    self.res = True
            elif word[0] !='.':
                if word[0] in node.dic:
                    self.dfs(node.dic[word[0]], word[1:])
            else:
                for v in node.dic.values():
                    self.dfs(v, word[1:])



if __name__ == '__main__':
  a = WordDictionary()
  a.addWord('bad')
  a.addWord('dad')
  a.addWord('mad')
  print a.search('pad')
  print a.search('bad')
  print a.search('.ad')
  print a.search('b..')
