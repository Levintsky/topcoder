"""
243. Shortest Word Distance (Easy)

Given a list of words and two words word1 and word2, return the shortest distance 
between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        id1_, id2_ = -1, -1
        n = len(words)
        best = n
        for i in range(n):
            if words[i] == word1:
                id1_ = i
                if id2_ >= 0:
                    best = min(best, i - id2_)
            if words[i] == word2:
                id2_ = i
                if id1_ >= 0:
                    best = min(best, i - id1_)
        return best
