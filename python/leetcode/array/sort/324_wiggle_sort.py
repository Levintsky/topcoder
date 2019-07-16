'''
324. Wiggle Sort II (Medium)

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

import statistics


class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

    def solve2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        median = statistics.median(nums)
        odd = []
        even = []
        medians = []
        for item in nums:
            if item < median - 1e-3:
                odd.append(item)
            elif item > median + 1e-3:
                even.append(item)
            else:
                medians.append(item)
        while len(medians) > 0:
            m = medians.pop()
            if len(odd) <= len(even):
                odd.append(m)
            else:
                even.append(m)
        odd = odd[::-1]
 
        for i in range(len(odd)):
            nums[2 * i] = odd[i]
            if i <= len(even) - 1:
                nums[2*i+1] = even[i]
    

if __name__ == '__main__':
  a = Solution()
  print(a.wiggleSort([1,5,1,1,6,4]))
  print(a.wiggleSort([1,3,2,2,3,1]))
