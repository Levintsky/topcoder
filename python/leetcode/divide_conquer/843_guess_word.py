"""
843. Guess the Word (Hard)

This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Note:  Any solutions that attempt to circumvent the judge will result in disqualification.
"""

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master(object):
    def __init__(self, secret):
        self.secret = secret

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        res = 0
        for i in range(6):
            if word[i] == self.secret[i]:
                res += 1
        return res

from collections import Counter


class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def distance(word1, word2):
            res = 0
            for i in range(6):
                if word1[i] == word2[i]:
                    res += 1
            return res
        n = len(wordlist)
        dis = []
        for i in range(n):
            dis.append([-1] * n)
        for i in range(n):
            for j in range(i+1, n):
                tmpd = distance(wordlist[i], wordlist[j])
                dis[i][j] = tmpd
                dis[j][i] = tmpd
        candidates = [i for i in range(n)]
        for i in range(10):
            # pick the one with min(max(#group))
            minidx, minmax_ = -1, n
            for idx in candidates:
                tmpdis = [dis[idx][j] for j in candidates]
                memo = Counter(tmpdis)
                tmp_max = max(memo.values())
                if tmp_max < minmax_:
                    minidx = idx
                    minmax_ = tmp_max
            tmp_w = wordlist[minidx]
            res = master.guess(tmp_w)
            if res == 6: return
            new_candidates = []
            for idx in candidates:
                if dis[minidx][idx] == res:
                    new_candidates.append(idx)
            candidates = new_candidates
            if len(candidates) == 0:
                return


if __name__ == "__main__":
    a = Solution()
    master = Master("acckzz")
    a.findSecretWord(["acckzz","ccbazz","eiowzz","abcczz"], master)