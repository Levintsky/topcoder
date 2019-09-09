"""
1178. Number of Valid Words for Each Puzzle (Hard)

With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
 

Example :

Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
 

Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] are English lowercase letters.
Each puzzles[i] doesn't contain repeated characters.
"""

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        memo, memo_inv = {}, {}
        for i in range(26):
            c = chr(ord('a') + i)
            memo[c] = set()
        for i, word in enumerate(words):
            for c in word:
                memo[c].add(i)
        whole_set = set(range(len(words)))
        for i in range(26):
            c = chr(ord('a') + i)
            memo_inv[c] = whole_set.difference(memo[c])

        result = []
        for p in puzzles:
            # process puzzle word
            stat = [False] * 26
            for c in p:
                ind = ord(c) - ord('a')
                stat[ind] = True
            # invalid set 1
            subset = set()
            for i in range(26):
                if not stat[i]:
                    c = chr(ord('a') + i)
                    subset = subset.union(memo[c])
            # invalid set 2
            first_c = p[0]
            subset2 = memo_inv[first_c]
            # intersect
            set3 = subset.intersection(subset2)
            res = len(subset) + len(subset2) - len(set3)
            result.append(len(words) - res)
        return result

    def solve2(self, words, puzzles):
        words_proc = []
        def proc(word):
            res = 0
            cnt = 0
            for i in range(26):
                c = chr(ord('a') + i)
                res = res << 1
                if c in word:
                    cnt += 1
                    res += 1
            if cnt <= 7:
                return res
            else:
                return -1

        for w in words:
            res = proc(w)
            if res > -1:
                words_proc.append(res)
        result = []
        for p in puzzles:
            p_proc = proc(p)
            tmp = 0

            p0_bit = 1 << (25 + ord('a') - ord(p[0]))
            for item in words_proc:
                if item & p_proc == item and p0_bit & item == p0_bit:
                    tmp += 1
            result.append(tmp)
        return result

    def solve3(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        count = collections.Counter("".join(sorted(set(w))) for w in words)
        res = []
        for p in puzzles:
            cur = 0
            for selector in itertools.product([0, 1], repeat=len(p) - 1):
                s = itertools.compress(p, [1] + list(selector))
                cur += count["".join(sorted(set(s)))]
            res.append(cur)
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
    print(a.solve2(["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
