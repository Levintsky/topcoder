"""
516. Longest Palindromic Subsequence (Medium)

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

"""
dp:
dp[i, j] := longest palindrome from i to j of substring s[i..j+1]

or bottom-up memoized dp?

n = len(s)
dp = [1] * n
for j in xrange(1, len(s)):
    pre = dp[j]
    for i in reversed(xrange(0, j)):
        tmp = dp[i]
        if s[i] == s[j]:
            dp[i] = 2 + pre if i + 1 <= j - 1 else 2
        else:
            dp[i] = max(dp[i + 1], dp[i])
        pre = tmp
return dp[0]
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        stat = {}
        result = self.helper(s, stat, 0, len(s)-1)
        print(stat)
        return result

    def helper(self, s, stat, i, j):
        # not AC, TLE
        if i>j: return 0
        if (i,j) in stat:
            return stat[(i,j)]
        if i == j:
            stat[(i,j)] = 1
        elif i+1 == j:
            if s[i] == s[j]: stat[(i,j)] = 2
            else: stat[(i,j)] = 1
        else:
            # memoized dp
            # i not included
            if s[i] == s[j]:
                stat[(i,j)] = 2+self.helper(s, stat, i+1, j-1)
            else:
                stat[(i,j)] = max(self.helper(s, stat, i+1, j), self.helper(s,stat,i,j-1))
        print(i,j,stat)
        return stat[(i,j)]

    def solution2(self, s):
        # still no AC, TLE
        n = len(s)
        first = [1] * n
        second = [0] * n
        step = 1
        while len(first) > 1:
            result = []
            for i in range(n-step):
                if s[i] == s[i+step]:
                    result.append(2+second[i+1])
                else:
                    result.append(max(first[i], first[i+1]))
            first, second = result, first
            print(first, second)
            step += 1
        return first[0]

    def solve3(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for j in range(n)]
        dp[n-1] = 1

        for i in range(n-1, -1, -1):   # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp
                    
        return dp[n-1]

    def solve4(self, s):
        n = len(s)
        if s == s[::-1]: return n # key step to make it faster
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp_new = dp[:]
            dp_new[i] = 1
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    dp_new[j] = 2 + dp[j+1]
                else:
                    dp_new[j] = max(dp_new[j+1], dp[j])
            dp = dp_new
        return dp[0]


if __name__ == '__main__':
    a = Solution()
    # print a.longestPalindromeSubseq('bbbab')
    # print a.longestPalindromeSubseq('cbbd')
    # print a.longestPalindromeSubseq('aabaa')
    print(a.solve3('bbbab'))
    # print(a.solution2('cbbd'))
    # print(a.solution2('aabaa'))
