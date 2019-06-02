"""
1071. Greatest Common Divisor of Strings (Easy)

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n1 = len(str1)
        n2 = len(str2)
        n = min(n1, n2)
        for i in range(n, 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                sub = str1[:i]
                if str1 == sub * (n1//i) and str2 == sub * (n2//i):
                    return sub
        return ""


if __name__ == "__main__":
    a = Solution()
    print(a.gcdOfStrings("ABCABC", "ABC"))
    print(a.gcdOfStrings("ABABAB", "ABAB"))
    print(a.gcdOfStrings("LEET", "CODE"))