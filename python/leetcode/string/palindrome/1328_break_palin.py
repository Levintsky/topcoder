"""
1328. Break a Palindrome (Medium)

Given a palindromic string palindrome, replace exactly one character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that isn't a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Example 2:

Input: palindrome = "a"
Output: ""
 

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        # case 1: not existing
        n = len(palindrome)
        if n == 1:
            return ""
        # case 2: all 'a'
        if palindrome == 'a' * n:
            res = 'a' * (n-1) + 'b'
            return res
        # case 3: aaaaxaaaa
        if n % 2 == 1:
            half = (n-1) // 2
            if palindrome[:half] == 'a' * half and palindrome[-half:] == 'a' * half:
                return palindrome[:-1] + 'b'
        # case 4: find first idx s.t. palindrome[idx] != 'a'
        i = 0
        while palindrome[i] == 'a':
            i += 1
        res = palindrome[:i] + 'a' + palindrome[i+1:]
        return res
        