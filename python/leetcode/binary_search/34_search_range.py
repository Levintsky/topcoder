'''
34. Search for a Range (Medium)

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

import bisect

class Solution(object):
    def solve2(self, nums, target):
        n = len(nums)
        ret = [-1, -1]
        i, j = 0, n - 1
        while i < j:
            mid = (i + j) / 2
            if nums[mid] < target: i = mid + 1
            else: j = mid
        if nums[i] != target: return ret
        else: ret[0] = i

        j = n - 1
        while i < j:
          mid = (i + j) / 2 + 1
          if nums[mid] > target: j = mid - 1
          else: i = mid
        ret[1] = i
        return ret

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return [-1, -1]
        if target < nums[0]: return [-1, -1]
        if target > nums[-1]: return [-1, -1]
        
        # step 1: first number smaller than target
        i, j = 0, n - 1
        while i < j:
            if nums[j] >= target: j-=1
            else: break
            mid = (i + j) / 2
            if nums[mid] >= target:
                j = mid - 1
            else:
                i = mid
        begin = max(i, j)
        if nums[begin] == target: pass
        elif nums[begin+1] == target: begin += 1
        else: return [-1, -1]
        
        # step 2: first number larger than target
        i, j = 0, n - 1
        while i < j:
            if nums[i] <= target: i += 1
            mid = (i + j) / 2
            if nums[mid] <= target:
                i = mid + 1
            else:
                j = mid
        end = min(i, j)
        if nums[end] == target: return [begin, end]
        else: return [begin, end-1]

    def solve3(self, nums, tareget):
        n = len(nums)
        id1 = bisect.bisect_left(nums, target)
        if id1 == n or nums[id1] != target: return [-1, -1]
        id2 = bisect.bisect(nums, target)
        return [id1, id2-1]


if __name__ == "__main__":
    a = Solution()
    print a.searchRange([0,0,1,2,3,3,4], 2)
    print a.solve2([0,0,1,2,3,3,4], 2)
    print a.searchRange([5, 7, 7, 8, 8, 10], 5)
    print a.solve2([5, 7, 7, 8, 8, 10], 5)
    print a.searchRange([5, 7, 7, 8, 8, 10], 7)
    print a.solve2([5, 7, 7, 8, 8, 10], 7)
    print a.searchRange([5, 7, 7, 8, 8, 10], 10)
    print a.solve2([5, 7, 7, 8, 8, 10], 10)
    print a.searchRange([5, 7, 7, 8, 8, 10], 6)
    print a.solve2([5, 7, 7, 8, 8, 10], 6)
