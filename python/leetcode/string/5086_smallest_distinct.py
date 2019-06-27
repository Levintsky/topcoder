"""
5086. Smallest Subsequence of Distinct Characters (Medium)

Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"

Note:

1 <= text.length <= 1000
text consists of lowercase English letters.
"""


class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        if len(text) == 0:
            return ""
        memo = {}  # c to earliest and latest
        for i, c in enumerate(text):
            if c not in memo:
                memo[c] = [i, i]
            else:
                memo[c][1] = i
        latest = list(memo.values())
        latest = [item[1] for item in latest]
        mlatest = min(latest)
        for i in range(26):
            c = chr(ord("a") + i)
            if c in memo and memo[c][0] <= mlatest:
                tmp = c
                # substring: text[i+1]..
                substr = ""
                start = memo[c][0] + 1
                for cc in text[start:]:
                    if cc != c:
                        substr += cc
                return c + self.smallestSubsequence(substr)


if __name__ == "__main__":
    a = Solution()
    # print(a.smallestSubsequence("cdadabcc"))
    print(a.smallestSubsequence("ecbacba"))
