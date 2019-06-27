"""
1044. Longest Duplicate Substring (Hard)

Given a string S, consider all duplicated substrings: (contiguous) substrings of 
S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length. (If S 
does not have a duplicated substring, the answer is "".)

Example 1:

Input: "banana"
Output: "ana"

Example 2:

Input: "abcd"
Output: ""

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
"""


class suffix(object):
    def __init__(self):
        self.index = 0
        self.rank = [0, 0]


def buildSuffixArray(txt, n):
    suffixes = []
    for i in range(n):
        suffixes.append(suffix())
        suffixes[i].index = i
        suffixes[i].rank[0] = ord(txt[i]) - ord("a")
        if i + 1 < n:
            suffixes[i].rank[1] = ord(txt[i + 1]) - ord("a")
        else:
            suffixes[i].rank[1] = -1

    suffixes.sort(key=lambda item: tuple(item.rank))
    ind = [0] * n

    k = 4
    while k < 2 * n:
        rank = 0
        prev_rank = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        ind[suffixes[0].index] = 0

        for i in range(1, n):
            if (
                suffixes[i].rank[0] == prev_rank
                and suffixes[i].rank[1] == suffixes[i - 1].rank[1]
            ):
                prev_rank = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank
            else:
                prev_rank = suffixes[i].rank[0]
                rank += 1
                suffixes[i].rank[0] = rank
            ind[suffixes[i].index] = i

        for i in range(n):
            nextindex = suffixes[i].index + k // 2
            suffixes[i].rank[1] = (
                suffixes[ind[nextindex]].rank[0] if nextindex < n else -1
            )

        sub_suffixes = suffixes[:n]
        sub_suffixes.sort(key=lambda item: tuple(item.rank))
        suffixes[:n] = sub_suffixes

        k *= 2

    suffixArr = []
    for i in range(n):
        suffixArr.append(suffixes[i].index)

    return suffixArr


def kasai(txt, suffixArr):
    n = len(suffixArr)
    lcp = [0] * n
    invSuff = [0] * n

    for i in range(n):
        invSuff[suffixArr[i]] = i

    k = 0
    for i in range(n):
        if invSuff[i] == n - 1:
            k = 0
            continue
        j = suffixArr[invSuff[i] + 1]
        while i + k < n and j + k < n and txt[i + k] == txt[j + k]:
            k += 1

        lcp[invSuff[i]] = k
        if k > 0:
            k -= 1
    return lcp


class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        suffixArr = buildSuffixArray(S, n)
        lcp = kasai(S, suffixArr)

        ans, start = 0, 0
        for i in range(n):
            if lcp[i] > ans:
                ans = lcp[i]
                start = suffixArr[i]
        if ans == 0:
            return ""
        else:
            return S[start : start + ans]

    def solve2(self, S):
        from functools import reduce

        A = [ord(c) - ord("a") for c in S]
        mod = 2 ** 63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)

        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res : res + lo]


if __name__ == "__main__":
    # trial
    array = buildSuffixArray("banana", 6)
    print(array)
    lcp = kasai("banana", array)
    print(lcp)

    a = Solution()
    print(a.solve2("banana"))
