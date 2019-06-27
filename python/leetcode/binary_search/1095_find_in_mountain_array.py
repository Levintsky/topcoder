"""
1095. Find in Mountain Array (Hard)

(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

Constraints:

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """


class MountainArray(object):
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        """
        :type index: int
        :rtype int
        """
        if index < 0 or index >= len(self.arr):
            raise RuntimeError
        return self.arr[index]

    def length(self):
        """
        :rtype int
        """
        return len(self.arr)


class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        # step 1: find the peak
        n = mountain_arr.length()
        i, j = 0, n - 1
        peak = None
        while i <= j:
            mid = (i + j) // 2
            # print(mid)
            num = mountain_arr.get(mid)
            if mid > 0:
                left = mountain_arr.get(mid - 1)
            else:
                left = None
            if mid != n - 1:
                right = mountain_arr.get(mid + 1)
            else:
                right = None
            if left is not None and num > left and right is not None and num > right:
                peak = mid
                break
            elif left is None or (num > left and right > num):
                i = mid + 1
            else:
                j = mid - 1
        # step 2: search in [0..peak]
        i, j = 0, peak
        if target == mountain_arr.get(peak):
            return peak
        while i <= j:
            mid = (i + j) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                j = mid - 1
            else:
                i = mid + 1
        # step 3: search in [peak..end-1]
        i, j = peak, n - 1
        if target == mountain_arr.get(peak):
            return peak
        while i <= j:
            mid = (i + j) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num < target:
                j = mid - 1
            else:
                i = mid + 1
        return -1


if __name__ == "__main__":
    a = Solution()
    # mountain_arr = MountainArray([1,2,3,4,5,3,1])
    # mountain_arr = MountainArray([3,5,3,2,0])
    mountain_arr = MountainArray([0, 2, 3, 5, 3])
    print(a.findInMountainArray(3, mountain_arr))
    mountain_arr = MountainArray([0, 1, 2, 4, 2, 1])
    print(a.findInMountainArray(3, mountain_arr))
