"""
1065. Index Pairs of a String (Easy)

Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

Example 1:
Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

Example 2:
Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

Note:

All strings contains only lowercase English letters.
It's guaranteed that all strings in words are different.
1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50
Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).
"""


class TrieNode(object):
    def __init__(self):
        self.next = [None] * 26
        self.is_word = False


class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # construct the trie
        root = TrieNode()
        for word in words:
            n = root
            for idx, c in enumerate(word):
                char_idx = ord(c) - ord("a")
                if n.next[char_idx] is None:
                    n.next[char_idx] = TrieNode()
                n = n.next[char_idx]
                if idx == len(word) - 1:
                    n.is_word = True
        result = []
        for i in range(len(text)):  # start i
            n = root
            for j in range(i, len(text)):
                c = text[j]
                cid = ord(c) - ord("a")
                if n.next[cid] is None:
                    break
                else:
                    n = n.next[cid]
                    if n.is_word:
                        result.append([i, j])
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.indexPairs("thestoryofleetcodeandme", ["story", "fleet", "leetcode"]))
    print(a.indexPairs("ababa", ["aba", "ab"]))
