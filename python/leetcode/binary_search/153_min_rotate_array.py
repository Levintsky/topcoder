'''
153. Find Minimum in Rotated Sorted Array (Medium)

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution(object):
  def findMin(self, nums):
    if len(nums) == 1:
      return nums[0]
    st = 0
    end = len(nums)-1
    while st != end:
      mid = (st + end) // 2
      if nums[st]<= nums[mid] and nums[mid] <= nums[end]:
        return nums[st]
      elif nums[st] > nums[mid]:
        end = mid
      elif nums[st] < nums[mid] and nums[mid] > nums[end]:
        st = mid+1
      elif st == end-1:
        return min(nums[st], nums[end])
    return nums[st]


if __name__ == '__main__':
  a = Solution()
  print a.findMin([4, 5, 6, 7, 0, 1, 2]) 
  print a.findMin(range(7)) 
  print a.findMin([2,1]) 
