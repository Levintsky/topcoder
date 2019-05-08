"""
154. Find Minimum in Rotated Sorted Array II (Hard)

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

class Solution(object):
  def findMin(self, nums):
    n = len(nums)
    i = 0
    j = n-1

    while i < j:
      if i == j-1:
        return min(nums[i], nums[j])
      mid = (i+j) / 2
      # case 1: sorted
      if nums[i] < nums[j]:
        return nums[i]
      # case 2: left-half
      elif nums[mid] < nums[i]:
        j = mid
      # case 3: right-half
      elif nums[mid] > nums[i]:
        i = mid
      else:
        i += 1
    return nums[mid]


if __name__ == "__main__":
  a = Solution()
  print(a.findMin([4,5,6,7,0,1,2]))
