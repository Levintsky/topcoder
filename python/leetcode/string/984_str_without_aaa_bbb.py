"""
984. String Without AAA or BBB (Medium)

Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"
 

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""

class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ""
        while A > 0 or B > 0:
            if A > B:
                nA, nB = min(2, A), min(1, B)
                if res == "" or res[-1] == 'b':
                    res += 'a' * nA + 'b' * nB
                else:
                	res += 'b' * nB + 'a' * nA
                A , B = A - nA, B - nB
            elif A < B:
                nA, nB = min(1, A), min(2, B)
                if res == "" or res[-1] == 'a':
                    res += 'b' * nB + 'a' * nA
                else:
                	res += 'a' * nA + 'b' * nB
                A, B = A - nA, B - nB
            else:
                if len(res) == 0 or res[-1] == 'B':
                    res += "ab" * A
                else:
                    res += "ba" * A
                A = 0
                B = 0
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.strWithout3a3b(1, 2))
    print(a.strWithout3a3b(4, 1))