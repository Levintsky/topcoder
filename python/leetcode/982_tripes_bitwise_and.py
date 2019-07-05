"""
982. Triples with Bitwise AND Equal To Zero (Hard)

Given an array of integers A, find the number of triples of indices (i, j, k) such that:

0 <= i < A.length
0 <= j < A.length
0 <= k < A.length
A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
 

Example 1:

Input: [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2
 

Note:

1 <= A.length <= 1000
0 <= A[i] < 2^16
"""

import collections


class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        memo = {}
        for item1 in A:
            for item2 in A:
                item = item1 & item2
                memo[item] = memo.get(item, 0) + 1
        res = 0
        for item1 in A:
            for item2 in memo.keys():
                if item1 & item2 == 0:
                    res += memo[item2]
        return res

    def solve2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        tmp = []
        maxlen = 0
        for a in A:
            tmp.append(bin(a)[2:])
            maxlen = max(maxlen, len(tmp[-1]))
        pool = []
        for s in tmp:
            extra = maxlen - len(s)
            pool.append('0'*extra + s)
        
        row, col = len(pool), len(pool[0])
        one = collections.defaultdict(set)
        for j in range(col):
            for i in range(row):
                if pool[i][j] == '1':
                    one[j].add(i)
        
        Venn = collections.defaultdict(list)
        cnt = 0
        for j in range(col):
            if len(one[j]) != 0:
                cnt += (len(one[j]))**3
                for i in range(j, 0, -1):
                    for prv in Venn[i]:
                        intersec = prv & one[j]
                        if len(intersec) != 0:
                            cnt += ((-1)**i)*(len(intersec))**3
                            Venn[i+1].append(intersec)
                Venn[1].append(one[j])
        
        return row ** 3 - cnt


if __name__ == "__main__":
    a = Solution()
    print(a.solve2([1,2,3]))
