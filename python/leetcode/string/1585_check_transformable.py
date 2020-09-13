"""
1585. Check If String Is Transformable With Substring Sort Operations (Hard)

Given two strings s and t, you want to transform string s into string t using the following operation any number of times:

Choose a non-empty substring in s and sort it in-place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".

Return true if it is possible to transform string s into string t. Otherwise, return false.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"
"84352" (from index 0 to 2) -> "34852"
Example 2:

Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"
Example 3:

Input: s = "12345", t = "12435"
Output: false
Example 4:

Input: s = "1", t = "2"
Output: false
 

Constraints:

s.length == t.length
1 <= s.length <= 105
s and t only contain digits from '0' to '9'.
"""


import collections


class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        qs = []
        for i in range(10):
            q = collections.deque()
            qs.append(q)
        
        for i, item in enumerate(s):
            item = ord(item) - ord('0')
            qs[item].append(i)
        print(qs)
        
        for item in t:
            idx = ord(item) - ord('0')
            if len(qs[idx]) == 0:
                return False
            # check legal
            rank = qs[idx][0]
            for j in range(idx):
                if len(qs[j]) > 0 and qs[j][0] < rank:
                    return False
            qs[idx].popleft()
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.isTransformable("84532", "34852"))
    print(a.isTransformable("34521", "23415"))
    print(a.isTransformable("12345", "12435"))
