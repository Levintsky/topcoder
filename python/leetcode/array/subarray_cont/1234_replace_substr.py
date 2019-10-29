"""
1234. Replace the Substring for Balanced String (Medium)

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.

Return 0 if the string is already balanced.

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".
 

Constraints:

1 <= s.length <= 10^5
s.length is a multiple of 4
s contains only 'Q', 'W', 'E' and 'R'.
"""

class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        nE = len(s) // 4
        memo = [0,0,0,0] # QWER
        def helper(tmplist, c, inc=True):
            diff = 1 if inc else -1
            if c == 'Q':
                tmplist[0] += diff
            elif c == 'W':
                tmplist[1] += diff
            elif c == 'E':
                tmplist[2] += diff
            else:
                tmplist[3] += diff

        def check_valid(curr, memo):
            flag = True
            for k in range(4):
                if curr[k] < memo[k]:
                    flag = False
            return flag

        for c in s:
            helper(memo, c)
            
        # find longest seq s.t.
        for i in range(4):
            memo[i] = max(memo[i]-nE, 0)
        if max(memo) == 0:
            return 0
        print(memo)
        ii = 0
        curr = [0,0,0,0]
        res = len(s)
        for jj in range(len(s)):
            helper(curr, s[jj])
            
            flag = check_valid(curr, memo)
            if flag:
                # move ii forward
                while check_valid(curr, memo):
                    helper(curr, s[ii], False)
                    ii += 1
                ii -= 1
                helper(curr, s[ii])
                res = min(res, jj-ii+1)
                # print(ii, jj)
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.balancedString("QWER"))
    print(a.balancedString("QQWE"))
    print(a.balancedString("QQQW"))
    print(a.balancedString("QQQQ"))
    print(a.balancedString("WQWRQQQW"))
