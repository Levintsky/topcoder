"""
745. Prefix and Suffix Search (Hard)

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
 

Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.
"""

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.memo = [None] * 26
        self.index = set()

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.root = TrieNode()
        self.root_inv = TrieNode()
        for i, word in enumerate(words):
            n = self.root
            for j, c in enumerate(word):
                n.index.add(i)
                ind = ord(c) - ord('a')
                if n.memo[ind] is None:
                    n.memo[ind] = TrieNode()
                n = n.memo[ind]
                if j == len(word) - 1:
                    n.is_word = True
                    n.index.add(i)

        for i, word in enumerate(words):
            n = self.root_inv
            wordinv = word[::-1]
            for j, c in enumerate(wordinv):
                n.index.add(i)
                ind = ord(c) - ord('a')
                if n.memo[ind] is None:
                    n.memo[ind] = TrieNode()
                n = n.memo[ind]
                if j == len(word) - 1:
                    n.is_word = True 
                    n.index.add(i)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        n = self.root
        for c in prefix:
            n = n.memo[ord(c) - ord('a')]
            if n is None: return -1
        set_pre = n.index
        n = self.root_inv
        for c in suffix[::-1]:
            n = n.memo[ord(c) - ord('a')]
            if n is None: return -1
        set_post = n.index
        set_ = set_pre & set_post
        if set_:
            return max(set_)
        else:
            return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

if __name__ == "__main__":
    a = WordFilter(["pop"])
    print(a.f("", "op"))
    # print(a.f('a', 'e'))
    # print(a.f('b', ''))
