"""
1593. Split a String Into the Max Number of Unique Substrings (Medium)

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.
"""

import pdb

class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.memo = []
        self.best = 0

        res = self.helper(s, 0)
        return self.best
        
    def helper(self, s, i):
        if i == len(s):
            # return True, len(self.memo)
            self.best = max(self.best, len(self.memo))
        for j in range(i+1, len(s)+1):
            if len(self.memo) + len(s) - j < self.best:
                return
            if s[i:j] not in self.memo:
                self.memo.append(s[i:j])
                self.helper(s, j)
                self.memo.pop()
        return


if __name__ == "__main__":
    a = Solution()
    # pdb.set_trace()
    print(a.maxUniqueSplit("ababccc"))
    print(a.maxUniqueSplit("aba"))
    print(a.maxUniqueSplit("aa"))
    print(a.maxUniqueSplit("addbsd"))
