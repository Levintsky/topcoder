"""
788. Rotated Digits (Easy)

X is a good number if after rotating each digit individually by 180 degrees, we 
get a valid number that is different from X.  Each digit must be rotated - we 
cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to 
themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the 
rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        s = set()
        res = 0
        N = str(N)
        for i, v in enumerate(N):
            # this iteration is magic #1
            # if 7xxxxx
            # the j goes over 0,1,2,5,6..xxxxx
            v = int(v)
            for j in range(v):
                if s.issubset(s2) and j in s2:
                    res += 7**(len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3**(len(N) - i - 1)
            # this is magic #2
            if v not in s2:
                return res
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))

    def solve2(self, N):
        # dp
        dp = [0] * (N + 1)
        count = 0
        for i in range(N+1):
            if i < 10:
                if i == 0 or i == 1 or i == 8:
                    dp[i] = 1
                elif i == 2 or i == 5 or i == 6 or i == 9:
                    dp[i] = 2
                    count += 1
            else:
                a, b = dp[i // 10], dp[i % 10]
                if a == 1 and b == 1: dp[i] = 1
                elif a >= 1 and b >= 1:
                    dp[i] = 2;
                    count += 1
        return count

    def solve3(self, N):
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])
        def isGood(x):    
            s = set([int(i) for i in str(x)])
            return s.issubset(s2) and not s.issubset(s1)
        return sum(isGood(i) for i in range(N + 1))

if __name__ == "__main__":
    a = Solution()
    print(a.solve2(2589))
    print(a.rotatedDigits(2589))