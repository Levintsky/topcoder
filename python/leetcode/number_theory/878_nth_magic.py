"""
878. Nth Magical Number (Hard)

A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: N = 1, A = 2, B = 3
Output: 2
Example 2:

Input: N = 4, A = 2, B = 3
Output: 6
Example 3:

Input: N = 5, A = 2, B = 4
Output: 10
Example 4:

Input: N = 3, A = 6, B = 4
Output: 8

Note:

1 <= N <= 10^9
2 <= A <= 40000
2 <= B <= 40000
"""

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        A, B = max(A, B), min(A, B)

        def common(a, b):
            if a % b == 0:
                return b
            else:
            	return common(b, a % b)
        cdg = common(A, B)
        factor = A * B // cdg
        w1 = int(N / (1+A/B-A/factor))
        w2 = int(N / (1+B/A-B/factor))
        res1 = w1 * A
        res2 = w2 * B

        def find(n, a, b, f, res):
            w = res // a
            cnt = w + res // b - res // f
            if cnt == N: return res % MOD
            elif cnt > n:
                while cnt > n:
                    res -= a
                    w -= 1
                    cnt = w + res // b - res // f
                if cnt == n: return res % MOD
            else:
                while cnt < n:
                    res += a
                    w += 1
                    cnt = w + res // b - res // f
                if cnt == n: return res % MOD
            return -1
        res1 = find(N, A, B, factor, res1)
        if res1 != -1: return res1
        res2 = find(N, B, A, factor, res2)
        return res2

    def solve2(self, N, A, B):
        a, b = A, B
        while b: a, b = b, a % b
        l, r, lcm = 2, 10**14, A * B / a
        while l < r:
            m = (l + r) / 2
            if m / A + m / B - m / lcm < N: l = m + 1
            else: r = m
        return l % (10**9 + 7)

if __name__ == "__main__":
    a = Solution()
    print(a.nthMagicalNumber(1, 2, 3))
    print(a.nthMagicalNumber(4, 2, 3))
    print(a.nthMagicalNumber(5, 2, 4))
    print(a.nthMagicalNumber(3, 6, 4))
    print(a.nthMagicalNumber(1000000000, 40000, 40000))
    print(a.nthMagicalNumber(887859796, 29911, 37516))