"""
1140. Stone Game II (Medium)

Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10 ^ 4
"""

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        self.memo = {}
        self.piles = piles
        x = self.dfs(0, 1)
        return x[0]

    def dfs(self, idx, M):
        # return res1, res2
        # edge case 1: existing
        if (idx, M) in self.memo:
            return self.memo[(idx, M)]
        # edge case 2:
        n = len(self.piles)
        if n - idx <= 2 * M:
            res = sum(self.piles[idx:])
            self.memo[(idx, M)] = (res, 0)
            return self.memo[(idx, M)]
        # iterative
        best = 0, 0
        for i in range(1, 2*M+1):
            # player 1 take i
            tmp = sum(self.piles[idx:idx+i])
            res = self.dfs(idx+i, max(M,i))
            final_res = tmp + res[1], res[0]
            if final_res[0] > best[0]:
                best = final_res
        self.memo[idx, M] = best
        return best


if __name__ == "__main__":
    a = Solution()
    print(a.stoneGameII([2,7,9,4,4]))