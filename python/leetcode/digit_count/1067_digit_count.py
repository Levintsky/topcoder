"""
1067. Digit Count in Range (Hard)

Given an integer d between 0 and 9, and two positive integers low and high as lower and upper bounds, respectively. Return the number of times that d occurs as a digit in all integers between low and high, including the bounds low and high.
 

Example 1:

Input: d = 1, low = 1, high = 13
Output: 6
Explanation: 
The digit d=1 occurs 6 times in 1,10,11,12,13. Note that the digit d=1 occurs twice in the number 11.
Example 2:

Input: d = 3, low = 100, high = 250
Output: 35
Explanation: 
The digit d=3 occurs 35 times in 103,113,123,130,131,...,238,239,243.
 

Note:

0 <= d <= 9
1 <= low <= high <= 2×10^8
"""

"""
Thinking 1:
A[n]: how many times d appears with <= n digit
B[n]: how many times d not appearing with <= n digit
C[n]: how many times d appearing at least somewhere

d > 0 case:
A[n] = 9B[n-1] + 10A[n-1] + C[n-1]
B[n] = 9^n
C[n] = 10^n - 9^n

for a number with n-digit: a1 a2 a3 a4 a5 ...
a1 > d: dxxxxxx (10^n-1) + (a1-1) A[n-1]
a1 == d: 
a1 < d
"""

"""
Thinking 2:
count by digit:
1. xxxxd: high // 10 + (last-digit >= d?)
2. xxxdx: (high // 100) * 10 + 
"""

class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        def count(N):
            if N == 0: return 0
            if d == 0 and N <= 10: return 0
            res = 0
            # xxxd
            if N % 10 > d:
                res += 1
            if N // 10 > 0:
                res += str(N // 10).count(str(d)) * (N % 10)
            if d > 0:
                res += N // 10
            else:
                res += N // 10 - 1
            # xxdx
            res += count(N // 10) * 10
            return res
        return count(high+1) - count(low)

    def solve2(self, d, low, high):
        def count(n, d):
            if n < 0 or n < d:
                return 0
            cnt = 0
            i = 1
            while i <= n:
                divider = i * 10
                cnt += (n // divider) * i
                if d > 0:
                    cnt += min(max(n % divider - d * i + 1, 0), i)
                else:
                    if n // divider > 0:
                        if i > 1:
                            cnt -= i
                            cnt += min(n % divider + 1, i)
                            if i != min(n % divider + 1, i):
                                print("diff!")
                i *= 10
            return cnt
        return count(high, d) - count(low-1, d)


if __name__ == "__main__":
    a = Solution()
    # print(a.digitsCount(1, 1, 2038))
    print(a.solve2(0, 1, 2038))