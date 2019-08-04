"""
1147. Longest Chunked Palindrome Decomposition (Hard)

Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

Each a_i is a non-empty string;
Their concatenation a_1 + a_2 + ... + a_k is equal to text;
For all 1 <= i <= k,  a_i = a_{k+1 - i}.

Example 1:

Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
Example 2:

Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
Example 3:

Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
Example 4:

Input: text = "aaa"
Output: 3
Explanation: We can split the string on "(a)(a)(a)".

Constraints:

text consists only of lowercase English characters.
1 <= text.length <= 1000
"""

class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        # find shortest left, right match
        # print(text)
        n = len(text)
        if n == 0:
            return 0
        cnt = 1
        while cnt * 2 <= n:
            # print(text[:cnt], text[-cnt:])
            if text[:cnt] == text[-cnt:]:
                break
            cnt += 1
        if cnt * 2 <= n:
            newtext = text[cnt:n-cnt]
            return 2 + self.longestDecomposition(newtext)
        else:
            return 1


if __name__ == "__main__":
    a = Solution()
    print(a.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
    print(a.longestDecomposition("merchant"))
    print(a.longestDecomposition("antaprezatepzapreanta"))
    print(a.longestDecomposition("aaa"))
    print(a.longestDecomposition("aaaa"))