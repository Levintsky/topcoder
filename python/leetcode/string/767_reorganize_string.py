"""
767. Reorganize String (Medium)

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

import collections

class Solution:
    def reorganizeString(self, S: str) -> str:
        memo = dict(collections.Counter(S))
        max_ = max(memo.values())
        rest = sum(memo.values()) - max_
        if max_ - rest >= 2:
            return ""

        pair = [(v, k) for k, v in memo.items()]
        pair.sort(reverse=True)
        print(pair)
        res = [pair[0][1]] * pair[0][0]
        idx = 0
        for v, k in pair[1:]:
        	for i in range(v):
        	    res[idx] += k
        	    idx = (idx+1) % max_
        return "".join(res)


if __name__ == "__main__":
    a= Solution()
    print(a.reorganizeString("aaab"))