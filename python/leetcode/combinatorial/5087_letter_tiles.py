"""
5087. Letter Tile Possibilities (Medium)

You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:

Input: "AAABBC"
Output: 188

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

from collections import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tc = Counter(tiles)
        mytc = list(tc.values())
        self.total = 0
        self.memo = {}
        self.memo_factor = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040}

        def comb(ttc):
            if max(ttc) == 0:
                return
            # ttc.sort()
            if tuple(ttc) not in self.memo:
                tmp = self.memo_factor[sum(ttc)]
                for item in ttc:
                    tmp //= self.memo_factor[item]
                self.total += tmp
                self.memo[tuple(ttc)] = tmp
            # else:
            #     self.total += self.memo[tuple(ttc)]
            print(ttc, self.total)
            for i in range(len(ttc)):
                if ttc[i] == 0:
                    continue
                new_ttc = [item for item in ttc]
                new_ttc[i] -= 1
                comb(new_ttc)

        comb(mytc)
        print(self.memo)
        return self.total


if __name__ == "__main__":
    a = Solution()
    print(a.numTilePossibilities("AAB"))
    print(a.numTilePossibilities("AAABBC"))
