"""
907. Sum of Subarray Minimums (Medium)

Given an array of integers A, find the sum of min(B), where B ranges over 
every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], 
[3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        stack = []
        curr = 0
        res = 0
        for i, item in enumerate(A):
            tmp_cnt = 1
            new = curr + item
            while stack and stack[-1][0] >= item:
                tmp, old_cnt = stack.pop()
                new -= (tmp - item) * old_cnt
                tmp_cnt += old_cnt
            stack.append((item, tmp_cnt))
            res = (res + new) % MOD
            curr = new % MOD
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.sumSubarrayMins([3,1,2,4]))
    print(a.sumSubarrayMins([81, 55, 2]))
