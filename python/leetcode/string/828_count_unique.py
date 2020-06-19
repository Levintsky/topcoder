"""
828. Count Unique Characters of All Substrings of a Given String (Hard)

"""

class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = []
        for i in range(26):
            memo.append([])
            
        for i, c in enumerate(s):
            idx = ord(c) - ord('A')
            memo[idx].append(i)
            
        size = len(s)
        MOD = 10 ** 9 + 7
        
        res = 0
        for i in range(26):
            n = len(memo[i])
            if n == 0:
                continue
            for j in range(n):
                if j > 0:
                    left = memo[i][j-1] + 1
                else:
                    left = 0
                if j < n - 1:
                    right = memo[i][j+1] - 1
                else:
                    right = size - 1
                res = (res + (memo[i][j] - left + 1) * (right - memo[i][j] + 1)) % MOD
        return res
        
