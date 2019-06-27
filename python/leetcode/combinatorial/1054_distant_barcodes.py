"""
1054. Distant Barcodes (Medium)

In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""

import collections


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        memo = collections.Counter(barcodes)
        memo = dict(memo)
        memo = [(memo[k], k) for k in memo.keys()]
        memo.sort(reverse=True)
        result = []
        for i in range(memo[0][0]):
            result.append([memo[0][1]])
        i = 0
        print(result)
        for idx in range(1, len(memo)):
            n, val = memo[idx]
            for j in range(n):
                result[i].append(val)
                i = (i + 1) % len(result)
        final = []
        for item in result:
            final += item
        return final


if __name__ == "__main__":
    a = Solution()
    print(a.rearrangeBarcodes([1, 1, 1, 2, 2, 2]))
    print(a.rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
