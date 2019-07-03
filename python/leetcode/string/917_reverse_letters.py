"""
917. Reverse Only Letters (Easy)

Given a string S, return the "reversed" string where all 
characters that are not a letter stay in the same place, and all 
letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""

class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        def isChar(c):
            if ord(c) >= ord("A") and ord(c) <= ord("Z"):
                return True
            if ord(c) >= ord("a") and ord(c) <= ord("z"):
                return True
            return False

        n = len(S)
        S = [c for c in S]
        i, j = 0, n-1
        while i < j:
            while not isChar(S[i]) and i < j:
                i += 1
            while not isChar(S[j]) and i < j:
                j -= 1
            if i < j:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
        res = "".join(S)
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.reverseOnlyLetters("ab-cd"))
    print(a.reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(a.reverseOnlyLetters("Test1ng-Leet=code-Q!"))

