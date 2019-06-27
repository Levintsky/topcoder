"""
942. DI String Match (Easy)

Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
 

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]
 

Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".
"""


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if S[0] == "I":
            result = [0, 1]
        else:
            result = [1, 0]

        min_, max_ = -1, 2
        for idx, c in enumerate(S[1:]):
            if c == "I":
                result.append(max_)
                max_ += 1
            else:
                result.append(min_)
                min_ -= 1
        result = [item - min_ - 1 for item in result]
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.diStringMatch("IDID"))
    print(a.diStringMatch("III"))
    print(a.diStringMatch("DDI"))
