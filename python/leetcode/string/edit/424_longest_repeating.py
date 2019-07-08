"""
424. Longest Repeating Character Replacement (Medium)

Given a string that consists of only uppercase English letters, you can replace 
any letter in the string with another letter at most k times. Find the length of a 
longest substring containing all repeating letters you can get after performing 
the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

"""
sliding window:
if in a substr, sum(stat) - max(stat) <= k,
  then replace all other chars with the most frequent char will be valid
else
  move start point to make this condition satisfy.
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
    :type s: str
    :type k: int
    :rtype: int
    """
        n = len(s)
        if n == 0:
            return 0

        st = 0
        stat = [0] * 26
        stat[ord(s[0]) - ord("A")] += 1

        max_ = 1
        for i in range(1, n):
            # add new stat
            stat[ord(s[i]) - ord("A")] += 1
            if sum(stat) - max(stat) <= k:
                max_ = max(max_, i - st + 1)
            else:
                while sum(stat) - max(stat) > k:
                    # remove st
                    stat[ord(s[st]) - ord("A")] -= 1
                    st += 1
        return max_


if __name__ == "__main__":
    a = Solution()
    print(a.characterReplacement("ABAB", 2))
    print(a.characterReplacement("AABABBA", 1))
