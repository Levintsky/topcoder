'''
132. Palindrome Partitioning II (Hard)

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

"""
Took me a while to understand. I'd like to help further explain it.

The definition of 'cut' array is the minimum number of cuts of a sub string. 
More specifically, cut[n] stores the cut number of string s[0, n-1].

Here is the basic idea of the solution:

Initialize the 'cut' array: For a string with n characters s[0, n-1], 
it needs at most n-1 cut. Therefore, the 'cut' array is initialized as cut[i] = i-1

Use two variables in two loops to represent a palindrome:
The external loop variable 'i' represents the center of the palindrome. The internal loop variable 'j' represents the 'radius' of the palindrome. Apparently, j <= i is a must.
This palindrome can then be represented as s[i-j, i+j]. If this string is indeed a palindrome, then one possible value of cut[i+j] is cut[i-j] + 1, where cut[i-j] corresponds to s[0, i-j-1] and 1 correspond to the palindrome s[i-j, i+j];

When the loops finish, you'll get the answer at cut[s.length]
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # logic is correct, but will TLE
        n = len(s)
        if n == 0: return 0
        odd = [1] * n
        even = [0] * (n-1)

        def longPalin(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return j - i - 1

        for ii in range(n):
            odd[ii] = longPalin(ii, ii)
        for ii in range(n-1):
            even[ii] = longPalin(ii, ii+1)
        # print('odd', odd)
        # print('even', even)
        
        result = [[1] * n] # len(1)
        # result[i][j]:
        #   substring of length (i+1), len == (n-i)
        for i in range(1, n):
            # ith iteration: result of substring length i+1
            # ..j | j+1..
            new_result = [i+1] * (n-i)
            for j in range(n-i):
                # str: j..j+i
                mid = j + i // 2
                if i % 2 == 1 and even[mid] >= i:
                    new_result[j] = 1
                    continue
                elif i % 2 == 0 and odd[mid] >= i:
                    new_result[j] = 1
                    continue
                else:
                    for k in range(j, j+i):
                        # j..k: result[k-j][j]
                        # k+1..j+i: result[j+i-k-1][k+1]
                        new_result[j] = min(new_result[j], result[k-j][j]+result[j+i-k-1][k+1])
            result.append(new_result)
            # print(result)
        return result[-1][0] - 1

    def solve2(self, s):
        # acceleration (problem specific)
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
 
        n = len(s)
        # cut[i]: result of s[0:i]
        cut = [0] * (n + 1)
        for i in range(n+1):
            cut[i] = i - 1

        # i: the middle of the palindrome
        for i in range(n):
            # odd palindrome
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j])
                j += 1
            # even
            j = 1
            while i-j+1 >= 0 and i+j<n and s[i-j+1] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j+1])
                j += 1
        return cut[n]


if __name__ == "__main__":
    a = Solution()
    print(a.minCut("aabaacaab"))
    # print(a.solve2("aa"))
