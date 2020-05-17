"""
1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

Given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
Example 4:

Input: n = 50, m = 100, k = 25
Output: 34549172
Explanation: Don't forget to compute the answer modulo 1000000007
Example 5:

Input: n = 37, m = 17, k = 7
Output: 418930126
 

Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
"""

class Solution(object):
    def numOfArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        # current_max, kk as key
        memo = {(-1, 0): 1}
        if k > m:
            return 0
        MOD = 10 ** 9 + 7

        for i in range(n):
            memo2 = {}
            for max_, kk in memo.keys():
                # new-val: max_+1..m
                # key updated as (new_val, kk+1)
                if kk <= k:
                    for v in range(max(1, max_+1), m+1):
                        k2 = (v, kk+1)
                        memo2[k2] = (memo2.get(k2, 0) + memo[max_, kk]) % MOD

                # new-val: 1..max_
                # key updated as (max_, kk)
                for v in range(1, max_+1):
                    k2 = (max_, kk)
                    memo2[k2] = (memo2.get(k2, 0) + memo[k2]) % MOD
                # print(max_, kk, memo2)
            keys = list(memo2.keys())
            for max_, kk in keys:
                if (m-max_)+kk < k: # not possible to meet
                    del memo2[max_, kk]
            memo = memo2
        # print(memo, k)
        res = 0
        for kv, r in memo.items():
            # print(kv)
            if kv[1] == k:
                # print(kv, r)
                res = (res + r) % MOD
        return res


if __name__ == "__main__":
    a = Solution()
    print(a.numOfArrays(2, 3, 1))
    print(a.numOfArrays(5, 2, 3))
    print(a.numOfArrays(9, 1, 1))
    print(a.numOfArrays(50, 100, 25))
    print(a.numOfArrays(37, 17, 7))