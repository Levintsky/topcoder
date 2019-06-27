"""
747. Largest Number At Least Twice of Others (Easy)

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.


Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = len(nums)
        if len_ == 1:
            return 0

        # init
        max1, max2 = None, None
        if nums[0] >= nums[1]:
            max1, max2 = 0, 1
        else:
            max1, max2 = 1, 0

        for i, item in enumerate(nums[2:], 2):
            if item >= nums[max1]:
                max1, max2 = i, max1
            elif item < nums[max1] and item >= nums[max2]:
                max2 = i
            # print(max1, max2, nums[max1], nums[max2])
        if nums[max1] >= 2 * nums[max2]:
            return max1
        else:
            return -1
