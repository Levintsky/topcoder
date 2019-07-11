"""
784. Letter Case Permutation (Easy)

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = [S]
        def is_char(c):
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                return True
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                return True
            
        def change(c):
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                idx = ord(c) - ord('a') + ord('A')
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                idx = ord(c) - ord('A') + ord('a')
            return chr(idx)
            
        for i, c in enumerate(S):
            new_result = []
            if is_char(c):
                for item in result:
                    item = item[:i] + change(c) + item[i+1:]
                    new_result.append(item)
                result += new_result
        return result