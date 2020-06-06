"""
303. Range Sum Query - Immutable (Easy)

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):
    # AC b/c weak test design
    def __init__(self, nums):
        """
    :type nums: List[int]
    """
        self.nums = [i for i in nums]

    def sumRange(self, i, j):
        """
    :type i: int
    :type j: int
    :rtype: int
    """
        x = self.nums[i : j + 1]
        return sum(x)


class NumArray(object):
    # AC. better solution if sumRange always called
    def __init__(self, nums):
        """
    :type nums: List[int]
    """
        self.cumul = [0]
        for i in range(len(nums)):
            self.cumul.append(self.cumul[-1] + nums[i])

    def sumRange(self, i, j):
        """
    :type i: int
    :type j: int
    :rtype: int
    """
        return self.cumul[j + 1] - self.cumul[i]
