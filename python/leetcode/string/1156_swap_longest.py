"""
1156. Swap For Longest Repeated Character Substring (Medium)

Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters. 

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
Example 3:

Input: text = "aaabbaaa"
Output: 4
Example 4:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
Example 5:

Input: text = "abcdef"
Output: 1
"""

class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        memo = []
        for i in range(26):
            memo.append([])
        i = 0
        n = len(text)
        while i < n:
            j = i + 1
            while j < n and text[j] == text[i]:
                j += 1
            ind = ord(text[i]) - ord('a')
            memo[ind].append((i, j-1))
            i = j
        best = 0
        for range_list in memo:
            for idx, tmptuple in enumerate(range_list):
                begin, end = tmptuple
                tmplen = end - begin + 1
                if len(range_list) > 1:
                    tmplen += 1
                best = max(best, tmplen)
                if idx > 0:
                    lbegin, lend = range_list[idx-1]
                    if lend + 2 == begin:
                        tmplen = end-begin+1+lend-lbegin+1
                        if len(range_list) >= 3:
                            tmplen += 1
                    else:
                        tmplen = end-begin+1+1
                    best = max(best, tmplen)
        return best


if __name__ == "__main__":
    a = Solution()
    print(a.maxRepOpt1("ababa"))
    print(a.maxRepOpt1("aaabaaa"))
    print(a.maxRepOpt1("aaabbaaa"))
    print(a.maxRepOpt1("aaaaa"))
    print(a.maxRepOpt1("abcdef"))
    print(a.maxRepOpt1("aabaadefaaa"))
    print(a.maxRepOpt1("aaaaabbbbbbaabbaabbaaabbbbab"))
