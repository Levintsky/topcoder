"""
702. Search in a Sorted Array of Unknown Size (Medium)

Given an integer array sorted in ascending order, write a 
function to search target in nums.  If target exists, then 
return its index, otherwise return -1. However, the array 
size is unknown to you. You may only access the array using 
an ArrayReader interface, where ArrayReader.get(k) returns 
the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, 
and if you access the array out of bounds, ArrayReader.get will 
return 2147483647.
"""

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) > target:
            return -1
        # get upper bound
        low, high = 0, 1
        while reader.get(high) < target:
            high *= 2
        # search in between
        while low <= high:
            mid = (low + high) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                high = mid - 1
            else:
            	low = mid + 1
        return -1



