"""
761. Special Binary String (Hard)

Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:
Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
Note:

S has length at most 50.
S is guaranteed to be a special binary string as defined above.
"""

class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        
        # preprocess
        cum = [0]
        for c in S:
            if c == '0':
                cum.append(cum[-1] - 1)
            else:
                cum.append(cum[-1] + 1)
        cum = cum[1:]
    
        print(cum)
        
        # find first (1, 0)
        i = 0
        flag = False
        while i < n-1 and not flag:
            if S[i] == '0' and S[i+1] == '1':
                # ii+1..i
                icum = cum[i]
                ii = i - 1
                while ii >= 0 and cum[ii] != icum:
                    ii -= 1
                left = S[ii+1:i+1]
                print(left)
                # i+1..j
                j = i + 1
                while cum[j] != cum[i]:
                    j += 1
                right = S[i+1:j+1]
                if right > left:
                    flag = True
                    S = S[:ii+1] + right + left + S[j+1:]
                else:
                    i += 1
            else:
                i += 1
        print(left, right, S)
        # return S
        if flag:
            return self.makeLargestSpecial(S)
        else:
            return S


if __name__ == "__main__":
    a = Solution()
    print(a.makeLargestSpecial("11011000"))
    # print(a.makeLargestSpecial("11101101100000"))
    # rint(a.makeLargestSpecial('11111001001000'))
