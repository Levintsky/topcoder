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

from collections import Counter


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

    def solve3(self, S):
        length = len(S)
        result = ""
        appeared = {}

        start = 0
        scan = 1
        i = start + 1
        while i < length - scan:
            appeared[S[start : start + scan]] = start
            if S[i : i + scan] not in appeared:
                appeared[S[i : i + scan]] = i
                i += 1
                continue

            s = appeared[S[i : i + scan]]
            print(s, S[i : i + scan], result)
            while i + scan < length and S[s + scan] == S[i + scan]:
                scan += 1
            result = S[s : s + scan]
            scan = len(result) + 1
            i = 1

        return result

    def solve4(self, S):
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord("a") for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 32

        # binary search, L = repeating string length
        left, right = 1, n
        while left != right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L

        start = self.search(left - 1, a, modulus, n, nums)
        return S[start : start + left - 1] if start != -1 else ""

    def search(self, L, a, modulus, n, nums):
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # compute the hash of string S[:L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus

        # already seen hashes of strings of length L
        seen = {h}
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    def solve5(self, S):
        sa = SuffixArrayInducedSort(S)
        bestlen, besti = max((v, i) for i, v in enumerate(sa.lcp))
        bestsuf = sa.suf[besti]
        return S[bestsuf : bestsuf + bestlen]

    def solve6(self, S):
        """
        :type S: str
        :rtype: str
        """
        nums = [ord(c)-ord('a') for c in S]
        l, r = 0, len(S)-1
        MOD = 10**9+7
        
        def check_valid(len_):
            key = 0
            n = len(nums)
            for item in nums[:len_]:
                key = (key * 26 + item) % MOD
            memo[key] = 1
            print(key)
            aL = (26 ** (len_ - 1)) % MOD
            for i in range(len_, n):
                key = key - nums[i-len_] * aL
                key = (key * 26 + nums[i]) % MOD
                if key in memo:
                    # print(key)
                    return True
                memo[key] = 1
            return False
        
        while l < r:
            memo = {} # hash key to set
            
            mid = (l+r) // 2
            
            if check_valid(mid):
                l = mid +1
            else:
                r = mid - 1
            print(mid, l, r)
        return l


class SuffixArrayInducedSort:
    def __init__(self, s):
        self._build_buckets(s)
        self._build_s_type()
        self._build_lms_suf()
        self._compute_suf()
        self._compute_lcp()

    def _build_buckets(self, s):
        buckets = sorted(Counter(s).items())
        indices = {c: i for i, (c, _) in enumerate(buckets)}
        self._string = list(map(indices.__getitem__, s))
        self._n = len(self._string)
        start = [1]
        for _, size in buckets:
            start.append(start[-1] + size)
        self._bucket_start = tuple(start[:-1])
        self._bucket_end = tuple(i - 1 for i in start[1:])

    def _build_s_type(self):
        s = self._string
        self._s_type = bytearray(self._n + 1)
        self._s_type[self._n] = True
        for i in range(self._n - 2, -1, -1):
            if s[i] < s[i + 1] or s[i] == s[i + 1] and self._s_type[i + 1]:
                self._s_type[i] = True

    def _is_lms(self, i):
        return i > 0 and self._s_type[i] and not self._s_type[i - 1]

    def _lms_equal(self, i, j):
        assert self._is_lms(i) and self._is_lms(j)
        if i == j:
            return True
        if i == self._n or j == self._n:
            return False
        k = 0
        while True:
            ilms = self._is_lms(i + k)
            jlms = self._is_lms(j + k)
            if k > 0 and ilms and jlms:
                return True
            if ilms != jlms or self._string[i + k] != self._string[j + k]:
                return False
            k += 1

    def _guess_suf(self):
        suf = [-1] * (self._n + 1)
        end = list(self._bucket_end)
        for i, c in enumerate(self._string):
            if not self._is_lms(i):
                continue
            suf[end[c]] = i
            end[c] -= 1
        suf[0] = self._n
        return self._induce_sort(suf)

    def _induce_sort(self, suf):
        start = list(self._bucket_start)
        for i in range(self._n + 1):
            j = suf[i] - 1
            if j < 0 or self._s_type[j]:
                continue
            c = self._string[j]
            suf[start[c]] = j
            start[c] += 1
        end = list(self._bucket_end)
        for i in range(self._n, -1, -1):
            j = suf[i] - 1
            if j < 0 or not self._s_type[j]:
                continue
            c = self._string[j]
            suf[end[c]] = j
            end[c] -= 1
        return suf

    def _build_lms_suf(self):
        suf = self._guess_suf()
        lms = [-1] * (self._n + 1)
        last = suf[0]
        lms[last] = 0
        assert last == self._n and self._is_lms(last)
        for i in range(1, self._n + 1):
            curr = suf[i]
            if not self._is_lms(curr):
                continue
            lms[curr] = lms[last]
            if not self._lms_equal(last, curr):
                lms[curr] += 1
            last = curr
        indices = [i for i, c in enumerate(lms) if c >= 0]
        summary = [c for c in lms if c >= 0]
        num_lms = len(summary)
        unique_lms = lms[last] + 1
        self._summary = summary
        self._summary_idx = indices
        if num_lms == unique_lms:
            self._summary_suf = [-1] * (num_lms + 1)
            self._summary_suf[0] = num_lms
            for i, c in enumerate(summary, 0):
                self._summary_suf[c + 1] = i
        else:
            self._summary_suf = SuffixArrayInducedSort(summary).suf

    def _compute_suf(self):
        suf = [-1] * (self._n + 1)
        end = list(self._bucket_end)
        num_lms = len(self._summary_idx)
        for j in range(num_lms, 1, -1):
            i = self._summary_idx[self._summary_suf[j]]
            c = self._string[i]
            suf[end[c]] = i
            end[c] -= 1
        suf[0] = self._n
        self.suf = self._induce_sort(suf)

    def _compute_lcp(self):
        n, s = self._n, self._string
        idx = [0] * (n + 1)
        for i, v in enumerate(self.suf):
            idx[v] = i
        self.lcp = [0] * (n + 1)
        k = 0
        for i in range(n + 1):
            if idx[i] == n:
                k = 0
                continue
            j = self.suf[idx[i] + 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            self.lcp[idx[i]] = k
            if k:
                k -= 1


if __name__ == "__main__":
    # trial
    """
    array = buildSuffixArray("banana", 6)
    print(array)
    lcp = kasai("banana", array)
    print(lcp)
    """
    a = Solution()
    # print(a.solve2("banana"))
    # print(a.solve3("banana"))
    # sa = SuffixArrayInducedSort("banana")
    # sa = SuffixArrayInducedSort("mississippi")
    # print(sa.lcp)
    # print(kasai("mississippi", [10, 7, 4, 1, 0, 9, 8, 6, 5, 3, 2]))
    print(a.solve6("banana"))
    # print(a.solve6("mississippi"))
