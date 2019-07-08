"""
792. Number of Matching Subsequences (Medium)

Given string S and a dictionary of words words, find the number of words[i] that is 
a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""

import bisect

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # log(n): binary search
        memo = {}
        for i in range(26):
            memo[i] = []
        for i, c in enumerate(S):
            idx = ord(c) - ord('a')
            memo[idx].append(i)
        res = 0
        for word in words:
            id_ = -1
            flag = True
            for i, c in enumerate(word):
                idx = ord(c) - ord('a')
                id2 = bisect.bisect_left(memo[idx], id_)
                if id2 == len(memo[idx]):
                    flag = False
                    break
                else:
                    id_ = memo[idx][id2]
                    if i < len(word) -1 and word[i] == word[i+1]:
                        id_ += 1
            if flag:
                res += 1
        return res


    def solve2(self, S, words):
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

if __name__ == "__main__":
    a = Solution()
    print(a.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))