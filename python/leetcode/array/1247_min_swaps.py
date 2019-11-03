"""
1247. Minimum Swaps to Make Strings Equal (Easy)

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

Example 2: 

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1
Example 4:

Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4

Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
"""

class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1x, s1y = 0, 0
        s2x, s2y = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    s1x += 1
                    s2y += 1
                else:
                    s1y += 1
                    s2x += 1
        if (s1x + s2x) % 2 == 1:
            return -1
        res = s1x // 2 + s1y // 2
        if s1x % 2 == 1:
            res += 2
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.minimumSwap('xx', 'yy'))
    print(a.minimumSwap('xy', 'yx'))
    print(a.minimumSwap('xx', 'xy'))
    print(a.minimumSwap("xxyyxyxyxx", "xyyxyxxxyx"))