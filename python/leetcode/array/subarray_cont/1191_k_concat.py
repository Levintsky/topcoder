"""
1191. K-Concatenation Maximum Sum (Medium)

Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0

Constraints:

1 <= arr.length <= 10^5
1 <= k <= 10^5
-10^4 <= arr[i] <= 10^4
"""

class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # case 1: all pos
        if min(arr) >= 0:
            tmp = sum(arr)
            res = tmp * k % MOD
            return res
        # case 2: all neg
        if max(arr) <= 0:
            return 0

        def helper(tmparr):
            # return max posible subarray sum
            min_, cum = 0, 0
            res = 0
            for item in tmparr:
                cum += item
                min_ = min(min_, cum)
                res = max(res, cum-min_, item)
            return res

        def helper2(tmparr):
            cum = 0
            res = 0
            for item in tmparr:
                cum += item
                res = max(res, cum)
            return res

        # case 3: k == 1
        if k == 1:
            return helper(arr) % MOD

        arrsum = sum(arr)
        # case 4: k == 2
        if k == 2 or arrsum <= 0:
            return helper(arr * 2) % MOD

        # pos sum generally
        mid = arrsum * (k-2)
        left = helper2(arr[::-1])
        right = helper2(arr)
        return (mid + left + right) % MOD


if __name__ == "__main__":
    a = Solution()
    print(a.kConcatenationMaxSum([1,2], 3))
    print(a.kConcatenationMaxSum([1,-2,1], 2))
    print(a.kConcatenationMaxSum([-1,-2], 7))
    print(a.kConcatenationMaxSum([3,-2,-2,3], 7))
    print(a.kConcatenationMaxSum([-5,4,-4,-3,5,-3], 3))
