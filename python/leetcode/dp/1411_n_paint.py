"""
1411. Number of Ways to Paint N × 3 Grid (Hard)

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000

"""

class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k:
                        result.append((i,j,k))
        memo = {}
        for item in result:
            memo[item] = 1
        MOD = 10 ** 9 + 7

        for i in range(n-1):
            memo2 = {}
            for key in result:
                memo2[key] = 0

            for key1 in result:
                for key2 in result:
                    res = [key1[i]!=key2[i] for i in range(3)]
                    if False not in res:
                        memo2[key2] = (memo2[key2]+memo[key1]) % MOD
            memo = memo2
        final_result = sum(memo.values()) % MOD
        return final_result


if __name__ == "__main__":
    a = Solution()
    print(a.numOfWays(1))
    print(a.numOfWays(2))
    print(a.numOfWays(3))
    print(a.numOfWays(7))
    print(a.numOfWays(5000))
