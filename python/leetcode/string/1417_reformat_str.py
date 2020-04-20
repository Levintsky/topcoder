"""
1417. Reformat The String (Easy)

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string. 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:

Input: s = "ab123"
Output: "1a2b3"
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        sd, sc = [], []
        for c in s:
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                sc.append(c)
            elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                sd.append(c)
        if len(sd) >= len(sc) + 2 or len(sc) >= len(sd) + 2:
            return ""
        sd = sd[::-1]
        sc = sc[::-1]
        ld, lc = len(sd), len(sc)
        id_, ic_ = 0, 0
        res = ""
        flag = len(sd) >= len(sc)
            
        while len(sd) > 0 or len(sc) > 0:
            if flag:
                c = sd.pop()
                res += c
            else:
                c = sc.pop()
                res += c
            flag = not flag
        return res
