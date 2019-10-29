"""
1239. Maximum Length of a Concatenated String with Unique Characters (Medium)

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
"""

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # remove not unique strings
        arr2 = []
        for s in arr:
            stat = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                stat[idx] += 1
            if max(stat) <= 1:
                arr2.append(s)
        arr = arr2

        def enc(s):
            res = 0
            for c in s:
                i = ord(c) - ord('a')
                res |= 1 << i
            return res

        memo = []
        for s in arr:
            memo.append(enc(s))

        res = {0: 0}
        for i, item in enumerate(memo):
            newres = {}
            for k, v in res.items():
                if k & item == 0:
                    newres[k|item] = max(newres.get(k|item, 0), res[k] + len(arr[i]))
            # add new thing s to res
            for k, v in newres.items():
                res[k] = max(res.get(k, 0), v)
            # print(res)
        return max(res.values())

    def solve(self, arr):
        


if __name__ == "__main__":
    a = Solution()
    print(a.maxLength(["un","iq","ue"]))
    print(a.maxLength(["cha","r","act","ers"]))
    print(a.maxLength(["abcdefghijklmnopqrstuvwxyz"]))
    print(a.maxLength(["yy","bkhwmpbiisbldzknpm"]))