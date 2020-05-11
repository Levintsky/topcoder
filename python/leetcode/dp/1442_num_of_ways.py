"""
1444. Number of Ways of Cutting a Pizza (Hard)

Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""

from functools import lru_cache

class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        m = len(pizza)
        n = len(pizza[0])
        self.memo = {}
        self.result = 0

        # k -= 1
        MOD = 10 ** 9 + 7

        # cumsum
        cumsum = []
        for i in range(m):
            cumsum.append([0] * n)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if pizza[0][0] == 'A':
                        cumsum[0][0] = 1
                elif i == 0:
                    cumsum[0][j] = cumsum[0][j-1]
                    if pizza[i][j] == 'A':
                        cumsum[i][j] += 1
                elif j == 0:
                    cumsum[i][0] = cumsum[i-1][0]
                    if pizza[i][j] == 'A':
                        cumsum[i][j] += 1
                else:
                    cumsum[i][j] = cumsum[i-1][j] + cumsum[i][j-1] - cumsum[i-1][j-1]
                    if pizza[i][j] == 'A':
                        cumsum[i][j] += 1 
        print(cumsum)

        def get_sum(li, lj, ri, rj):
            if li > ri or lj > rj:
                return 0
            if li == 0 and lj == 0:
                res = cumsum[ri][rj]
            elif li == 0:
                res = cumsum[ri][rj] - cumsum[ri][lj-1]
            elif lj == 0:
                res = cumsum[ri][rj] - cumsum[li-1][rj]
            else:
                res = cumsum[ri][rj] + cumsum[li-1][lj-1] - cumsum[li-1][rj] - cumsum[ri][lj-1]
            return res

        def memo_dp(li, lj, ri, rj, kk):
            if (li, lj, kk) in self.memo:
                return self.memo[(li, lj, kk)]
            # edge case
            if kk == 1:
                return 1
            elif kk == 2:
                result = 0
                # horizontal from up
                # ii = li
                # while ii < ri: # get_sum(li, lj, ii, rj) == 0:
                #     ii += 1
                for ii in range(li, ri):
                    if get_sum(li, lj, ii, rj) > 0 and get_sum(ii+1, lj, ri, rj) > 0:
                        result += 1

                for jj in range(lj, rj):
                    if get_sum(li, lj, ri, jj) > 0 and get_sum(li, jj+1, ri, rj) > 0:
                        result += 1

                result = result % MOD
                self.memo[(li, lj, kk)] = result
                return result
            else: # not edge
                result = 0
                # horizontal from up

                for ii in range(li, ri):
                    if get_sum(li, lj, ii, rj) > 0 and get_sum(ii+1, lj, ri, rj) > 0:
                        result += memo_dp(ii+1, lj, ri, rj, kk-1)
                for jj in range(lj, rj):
                    if get_sum(li, lj, ri, jj) > 0 and get_sum(li, jj+1, ri, rj) > 0:
                        result += memo_dp(li, jj+1, ri, rj, kk-1)

                result = result % MOD
                self.memo[(li, lj, kk)] = result
                return result

        result = memo_dp(0, 0, m-1, n-1, k)
        # print(self.memo)
        return result, self.memo # self.memo[(0, 0, k-1)]

    def solve2(self, pizza, K):
        MOD = 10 ** 9 + 7
        n, m = len(pizza), len(pizza[0])
        num_apples = [[0] * (m + 1) for _ in range(n + 1)]
        memo = {}
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                num_apples[i][j] = (j + 1 < m and num_apples[i][j + 1]) + \
                                   (i + 1 < n and num_apples[i + 1][j]) - \
                                   (i + 1 < n and j + 1 < m and num_apples[i + 1][j + 1]) + \
                                   int(pizza[i][j] == 'A')
        print(num_apples)
                
        def is_valid(x0, y0, x1=n-1, y1=m-1):
            '''inclusive'''
            if x0 > x1 or y0 > y1: return False
            num = num_apples[x0][y0] - \
                  num_apples[x1 + 1][y0] - \
                  num_apples[x0][y1 + 1] + \
                  num_apples[x1 + 1][y1 + 1]
            return num > 0
        
        @lru_cache(None)
        def num_ways(x, y, k):
            if not is_valid(x, y): return 0
            if k == 1: return 1
            res = 0
            # cut horizontally
            for j in range(y, m - 1):
                if is_valid(x, y, n - 1, j):
                    res = (res + num_ways(x, j + 1, k - 1)) % MOD
            # cut vertically                    
            for i in range(x, n - 1):
                if is_valid(x, y, i, m - 1):
                    res = (res + num_ways(i + 1, y, k - 1)) % MOD
            memo[(x, y, k)] = res
            return res
        
        res = num_ways(0, 0, K)
        return res, memo


if __name__ == "__main__":
    a = Solution()
    """
    print(a.ways(["AAA","..."], 2))
    print(a.ways(["A..","AAA","..."], 3))
    print(a.ways(["....","AAAA","...."], 2))

    print(a.ways(["A...","AAAA","...."], 3))
    """

    r1, m1 = a.ways([".A..A","A.A..","A.AA.","AAAA.","A.AA."], 5)
    # print(m1)
    # print(a.ways([".A..","A.A.","A.AA","AAAA"], 4))
    # print(a.solve2([".A..","A.A.","A.AA","AAAA"], 4))

    # r1, m1 = a.ways(["A.AA."], 4)
    print(r1, m1)
    # r2, m2 = a.solve2(["A.AA."], 2)
    # print(r1, r2)
    """
    print(m1)
    print(m2)
    print('diff')
    for k in m2.keys():
        i, j, kk = k
        if (i, j, kk) in m1.keys():
            if m2[k] != m1[i,j,kk]:
                print(i, j, kk, m2[k], m1[i,j,kk])
    """
