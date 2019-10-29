"""
1240. Tiling a Rectangle with the Fewest Squares (Hard)

Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

Example 1:

Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)

Example 2:

Input: n = 5, m = 8
Output: 5

Example 3:

Input: n = 11, m = 13
Output: 6

Constraints:

1 <= n <= 13
1 <= m <= 13
"""

class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # make co prime
        def gcd(i, j):
            # i < j always
            if j % i == 0:
                return i
            else:
                return gcd(j%i, i)
        m, n = min(m, n), max(m, n)
        tmpgcd = gcd(m, n)
        m //= tmpgcd
        n //= tmpgcd
        
        memo = []
        memo.append([1]) # 1
        memo.append([2,1]) # 2
        memo.append([3,3,1]) # 3
        memo.append([4,2,4,1]) # 4
        memo.append([5,4,4,5,1]) # 5
        memo.append([6,3,2,3,5,1]) # 6
        memo.append([7,5,5,5,5,5,1]) # 7
        memo.append([8,4,5,2,5,4,7,1]) # 8
        memo.append([9,6,3,6,6,3,6,7,1]) # 9
        memo.append([10,5,6,4,2,4,6,5,6,1]) # 10
        memo.append([11,7,6,6,6,6,6,6,7,6,1]) # 11
        memo.append([12,6,4,3,6,2,6,3,4,5,7,1]) # 12
        memo.append([13,8,7,7,6,6,6,6,7,7,6,7,1]) # 13
        return memo[n-1][m-1]

    def solve(self, n, m):
        # not correct
        # make co prime
        def gcd(i, j):
            # i < j always
            if j % i == 0:
                return i
            else:
                return gcd(j%i, i)
        m, n = min(m, n), max(m, n)
        tmpgcd = gcd(m, n)
        m //= tmpgcd
        n //= tmpgcd
        mm, nn = m, n

        # solve it recursively
        self.memo = {(1, 1): 1}
        for m in range(1, mm+1):
            for n in range(1, nn+1):
                self.memo[m,n] = self.euclid(m, n)
                # patterns 1:
                for i in range(1, m):
                    for j in range(1, n):
                        for k in range(1, min(m-i, j)):
                            res = self.memo[i,j] + self.memo[i+k,n-j] + 1 \
                                + self.memo[m-i-k, n-j+k] + self.memo[m-i, j-k]
                            self.memo[m,n] = min(self.memo[m,n], res)
        return self.memo[mm,nn]

    def euclid(self, i, j):
        i, j = max(i, j), min(i, j)
        if j == 0:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i,j)]
        elif i == j:
            return 1
        else:
            res = 1 + self.euclid(i-j, j)
            self.memo[(i,j)] = res
            self.memo[(j,i)] = res
            return res

    def solve2(self, n, m):
        # dfs
        curr = [0] * m
        self.res = m * n

        def dfs(curr, tmpres):
            # 0. prune
            if tmpres > self.res:
                return
            # 1. check full
            flag = True
            for item in curr:
                if item < n:
                    flag = False
            if flag:
                self.res = min(self.res, tmpres)
                return
            # 2. find lowest, left-most
            index = 0
            for i, item in enumerate(curr):
                if item < curr[index]:
                    index = i
            # maximum possible
            max_h = n - curr[index]
            j = index + 1
            while j < m and curr[j] == curr[index]:
                j += 1
            # recursive
            e = min(max_h, j-index)
            while e >= 1:
                for i in range(index, index+e):
                    curr[i] += e
                dfs(curr, tmpres+1)
                for i in range(index, index+e):
                    curr[i] -= e
                e -= 1
            return

        dfs(curr, 0)
        return self.res


if __name__ == "__main__":
    a = Solution()
    """
    print(a.tilingRectangle(2, 3))
    print(a.tilingRectangle(5, 8))
    print(a.tilingRectangle(11, 13))
    print(a.tilingRectangle(6, 4))
    """
    for i in range(1, 14):
        for j in range(1, i):
            res1, res2 = a.tilingRectangle(i, j), a.solve2(i, j)
            if res1 != res2:
                print(i, j, res1, res2)