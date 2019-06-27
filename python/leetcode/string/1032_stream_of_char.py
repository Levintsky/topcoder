"""
1032. Stream of Characters (Hard)

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""

"""
Keypoints:
Use a reverse Trie
"""

import collections
from functools import reduce


class TrieNode(object):
    def __init__(self):
        self.mapping = [None] * 26
        self.is_word = False


class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = TrieNode()
        # step 1: build a trie
        for word in words:
            n = self.root
            word = word[::-1]
            for idx, c in enumerate(word):
                cid = ord(c) - ord("a")
                if n.mapping[cid] is None:
                    n.mapping[cid] = TrieNode()
                n = n.mapping[cid]
                if idx == len(word) - 1:
                    n.is_word = True
        # step 2: keep a dict mapping active suffix to nodes:
        # self.active_list = {"": self.root}
        self.active_str = ""

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.active_str += letter
        n = self.root
        for c in self.active_str[::-1]:
            cid = ord(c) - ord("a")
            if n.mapping[cid] is not None:
                n = n.mapping[cid]
                if n.is_word:
                    return True
            else:
                break
        return False

        """
        result = False
        # to_del = []
        new_active_list = {"": self.root}
        for k in self.active_list.keys():
        	cid = ord(letter) - ord('a')
        	n = self.active_list[k].mapping[cid]
        	if n is not None:
        		new_active_list[k+letter] = n
        		if n.is_word:
        			result = True
        self.active_list = new_active_list
        """
        # for item in to_del:
        # 	del self.active_list[k]
        # if "" not in self.active_list:
        # 	self.active_list[""] = self.root
        # print(self.active_list.keys())

        return result


class StreamChecker2(object):
    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words:
            reduce(dict.__getitem__, w, self.trie)["#"] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [
            node[letter] for node in self.waiting + [self.trie] if letter in node
        ]
        return any("#" in node for node in self.waiting)


if __name__ == "__main__":
    streamChecker = StreamChecker(["cd", "f", "kl"])
    query_list = "abcdefghijkl"
    for c in query_list:
        print(c, streamChecker.query(c))
    """
    print(streamChecker.query('b'))
    print(streamChecker.query('c'))
    print(streamChecker.query('d'))
    print(streamChecker.query('e'))
    print(streamChecker.query('f'))
    print(streamChecker.query('g'))
    print(streamChecker.query('h'))
    print(streamChecker.query('i'))
    print(streamChecker.query('j'))
    print(streamChecker.query('k'))
    print(streamChecker.query('l'))
    """
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
