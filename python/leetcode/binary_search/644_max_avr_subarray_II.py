"""
644. Maximum Average Subarray II (Hard)

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = float(min(nums))
        r = float(max(nums))
        if k == 1:
            return r

        while r - l >= 1e-5:
            mid = (l + r) / 2.0

            if self.check_valid(nums, mid, k):
                l = mid
            else:
                r = mid

        return l

    def check_valid(self, nums, mid, k):
        n = len(nums)
        min_pre = 0
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1] - mid
            if i >= k and sums[i] - min_pre >= 0:
                return True
            if i >= k:
                min_pre = min(min_pre, sums[i - k + 1])
        return False


if __name__ == "__main__":
    a = Solution()
