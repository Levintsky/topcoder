"""
1092. Shortest Common Supersequence (Hard)

Given two strings str1 and str2, return the shortest string that has both 
str1 and str2 as subsequences.  If multiple answers exist, you may return any 
of them.

(A string S is a subsequence of string T if deleting some number of characters 
from T (possibly 0, and the characters are chosen anywhere from T) results in 
the string S.)

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a substring of "cabac" because we can delete the first "c".
str2 = "cab" is a substring of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1.find(str2) >= 0:
            return str1
        if str2.find(str1) >= 0:
            return str2

        def produce_common(s1, s2):
            # s1..s2
            overlap = min(len(s1), len(s2)) - 1
            while overlap > 0:
                if s1[-overlap:] == s2[:overlap]:
                    return s1 + s2[overlap:]
                overlap -= 1
            return s1 + s2

        res1 = produce_common(str1, str2)
        res2 = produce_common(str2, str1)
        if len(res1) <= len(res2):
            return res1
        else:
            return res2

    def solve2(self, str1, str2):
        res1 = self.find_(str1, str2)
        res2 = self.find_(str2, str1)
        print(res1)
        print(res2)
        if len(res1) <= len(res2):
            return res1
        else:
            return res2

    def find_(self, st1, st2):
        start = -1
        len_ = -1
        n1, n2 = len(st1), len(st2)
        for start_j in range(n2):
            j = start_j
            for i in range(n1):
                if st1[i] == st2[j]:
                    j += 1
                if j == n2:
                    break
            tmplen_ = j - start_j
            if tmplen_ > len_:
                start = start_j
                len_ = tmplen_
        res = st1
        if start > 0:
            res = st2[:start] + res
        res += st2[start + len_ :]
        return res

    def solve3(self, str1, str2):
        # longest common
        n1 = len(str1)
        n2 = len(str2)
        result = []
        for i in range(n1 + 1):
            result.append([[0, ""] for _ in range(n2 + 1)])
        for i in range(n1):
            for j in range(n2):
                if str1[i] == str2[j]:
                    result[i + 1][j + 1] = [
                        result[i][j][0] + 1,
                        result[i][j][1] + str1[i],
                    ]
                elif result[i][j + 1][0] >= result[i + 1][j][0]:
                    result[i + 1][j + 1] = [item for item in result[i][j + 1]]
                else:
                    result[i + 1][j + 1] = [item for item in result[i + 1][j]]
        # print(result[-1][-1])
        longest = result[n1][n2][1]
        n3 = len(longest)
        i, j, k = 0, 0, 0
        res = ""
        while i < n1 or j < n2:
            if k == n3:
                res += str1[i:]
                res += str2[j:]
                break
            if i < n1:
                while str1[i] != longest[k]:
                    res += str1[i]
                    i += 1
            if j < n2:
                while str2[j] != longest[k]:
                    res += str2[j]
                    j += 1
            res += longest[k]
            k += 1
            i += 1
            j += 1
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.solve3("abac", "cab"))
    print(a.solve3("bbbaaaba", "bbababbb"))
