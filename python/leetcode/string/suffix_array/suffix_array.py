from collections import Counter


class SuffixArrayInducedSort(object):
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
        return


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
    
    max_len = max(lcp)
    for i, item in lcp:
        if lcp[i] == max_len:
            start = suffixArr[i]
            return txt[start:start+max_len]
    # return lcp


if __name__ == "__main__":
    # s = "mississippi" # "banana"
    s = "zrziy"
    suffix = SuffixArrayInducedSort(s)
    max_substr = suffix.suf[-1]
    print(s[max_substr:])
    # print(kasai(s, suffix.suf[1:]))
