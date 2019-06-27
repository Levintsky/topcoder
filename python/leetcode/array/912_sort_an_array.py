"""
912. Sort an Array (Medium)

Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]

Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Note:

1 <= A.length <= 10000
-50000 <= A[i] <= 50000
"""

"""
Quicksort:
partition logic
0. i = left-1
1. nums[left] .. nums[i], all <= pivot
  if nums[j] > pivot, do nothing
  if nums[j] <= pivot, 
2. at the end, swap nums[i+1], nums[right]

quicksort on left..i and i+2..right
swap nums
"""

import random


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def quicksort(left, right):
            print("working on:", left, right, nums[left : right + 1])
            # print('before', left, right, nums[left:right+1])
            if left >= right:
                return
            # find a pivot
            ind = random.randint(left, right)
            nums[ind], nums[right] = nums[right], nums[ind]
            # print('pivot', left, right, nums[left:right+1])
            pivot = nums[right]
            l, r = left, right - 1
            while l < r:
                while nums[l] < pivot and l < r:
                    l += 1
                while nums[r] > pivot and r > l:
                    r -= 1
                if nums[l] >= pivot and nums[r] <= pivot and l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
            # now l == r
            # print('b', left, right, nums[left:l], nums[l], nums[l+1:right+1])
            if nums[l] >= pivot:  # pivot not the largest
                nums[l], nums[right] = nums[right], nums[l]
                quicksort(left, l - 1)
                quicksort(l + 1, right)
            else:
                quicksort(left, l)
            # print('after', left, right, nums[left:right+1])
            # print(left, right, nums[left:l], nums[l], nums[l+1:right+1])

        def quicksort2(left, right):
            if left >= right:
                return
            i = left - 1
            ind = random.randint(left, right)
            nums[ind], nums[right] = nums[right], nums[ind]
            pivot = nums[right]
            for j in range(left, right):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[right] = nums[right], nums[i + 1]
            quicksort2(left, i)
            quicksort2(i + 2, right)

        quicksort2(0, len(nums) - 1)
        return nums


if __name__ == "__main__":
    a = Solution()
    array = [5, 2, 3, 1]
    print(a.sortArray(array))
    array = [5, 1, 1, 2, 0, 0]
    print(a.sortArray(array))
    array = [1, 3, 5, 7, 2, 8, 6, 4]
    print(a.sortArray(array))
    # array = [-19945, -19989, -19983, -19979, -19958, -19956, -19995, -19979, -19945, -19951, -19979, -19956, -19987, -19984]
    # print(a.sortArray(array))
