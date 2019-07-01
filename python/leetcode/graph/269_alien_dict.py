"""
269. Alien Dictionary (Hard)

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        map_ = {}
        n = len(words)

        # all the characters
        c_set = set()
        for word in words:
            for c in word:
                c_set.add(c)

        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]
            n1, n2 = len(w1), len(w2)
            j = 0
            while j < min(n1, n2) and w1[j] == w2[j]:
                j += 1
            if j != n1:
                c1, c2 = w1[j], w2[j]
            if c1 not in map_:
                map_[c1] = []
            map_[c1].append(c2)
        # stat of in-degrees
        in_deg_ = {}
        for c in c_set:
            in_deg_[c] = 0
        for k in map_.keys():
            for item in map_[k]:
                in_deg_[item] += 1
        print(in_deg_)
        set0 = []
        for c in in_deg_.keys():
            if in_deg_[c] == 0: set0.append(c)

        result = ""
        while len(set0) != 0:
            new_set0 = []
            for c in set0:
                result += c
                c_set.remove(c)
                if c not in map_: continue
                for item in map_[c]:
                    in_deg_[item] -= 1
                    if in_deg_[item] == 0:
                        new_set0.append(item)
            set0 = new_set0

        if len(c_set) == 0:
            return result
        else:
            return ""

    def solve2(self, words):
        # step 0: get all characters
        n = len(words)
        alphabets = set()
        for word in words:
            for c in word:
                alphabets.add(c)
        
        # step 1: get dag
        # memo: c: prev_set
        memo_cnt = {}
        memo_char = {}
        for c in alphabets:
            memo_cnt[c] = 0
            memo_char[c] = set()
        zero_list = list(alphabets)
        for i in range(n-1):
            # compare words[i] and words[i+1]
            idx = 0
            prevc, nextc = None, None
            while idx < len(words[i]) and idx < len(words[i+1]):
                if words[i][idx] != words[i+1][idx]:
                    prevc = words[i][idx]
                    nextc = words[i+1][idx]
                    break
                idx += 1
            if prevc is not None:
                if nextc not in memo_char[prevc]:
                    memo_cnt[nextc] += 1
                    memo_char[prevc].add(nextc)
                if nextc in zero_list:
                    zero_list.remove(nextc)
        # step 2: topological sort
        res = []
        while len(zero_list) > 0:
            c = zero_list.pop()
            res.append(c)
            for nextc in memo_char[c]:
                memo_cnt[nextc] -= 1
                if memo_cnt[nextc] == 0:
                    zero_list.append(nextc)
            memo_char[c] = set()
        if len(res) == len(alphabets):
            return "".join(res)
        else:
            return ""

if __name__ == "__main__":
    a = Solution()
    arr = ["wrt", "wrf", "er", "ett", "rftt"]
    # arr = ["z", "x"]
    # arr = ["z", "x", "z"]
    # arr = ["z", "z"]
    # print(a.alienOrder(arr))
    print(a.solve2(arr))
