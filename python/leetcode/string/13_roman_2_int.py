"""
13. Roman to Integer (Easy)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec = []
        rec.append(("M", "-", "-"))
        rec.append(("C", "D", "M"))
        rec.append(("X", "L", "C"))
        rec.append(("I", "V", "X"))
        result = 0
        i = 0
        while s != "":
            tmp = 0
            c1, c2, c3 = rec[i]
            if s.startswith(c1 + c2):
                tmp = 4
                s = s[2:]
            elif s.startswith(c1 + c3):
                tmp = 9
                s = s[2:]
            else:
                if s.startswith(c2):
                    tmp = 5
                    s = s[1:]
                j = 0
                while j < len(s) and s[j] == c1:
                    j += 1
                tmp += j
                s = s[j:]
            result += tmp * (10 ** (3 - i))

            i += 1
        return result
