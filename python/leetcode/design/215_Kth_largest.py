'''
215. Kth Largest Element in an Array (Medium)

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <= array's length.
'''
import sys


class Solution(object):
  def findKthLargest(self, nums, k):
    #
    n = len(nums)
    if n == 1:
      return nums[0]
    min_heap = [] # to keep largest update

    for item in nums:
      if k == 0:
        min_heap.append(item)
        n += 1
      elif len(min_heap) < k: # insert to the heap
        min_heap.append(item)
        # adjust: swap if necessary
        j = len(min_heap) - 1
        while(j>0 and min_heap[j]<min_heap[(j-1)/2]):
          min_heap[j], min_heap[(j-1)/2] = min_heap[(j-1)/2], min_heap[j]
          j = (j-1)/2
        n += 1
      else: # already k
        if item > min_heap[0]:
          min_heap[0] = item
          j = 0
          while(j<len(min_heap)-1):
            l_index = j * 2 + 1
            r_index = j * 2 + 2
            if l_index<len(min_heap):
              l_value = min_heap[l_index]
            else:
              l_value = sys.maxint
            if r_index<len(min_heap):
              r_value = min_heap[r_index]
            else:
              r_value = sys.maxint
            print min_heap[j], l_value, r_value
            # if left is smaller, < min_heap[j], swap left
            if l_value<min_heap[j] and l_value<=r_value:
              min_heap[j], min_heap[l_index] = min_heap[l_index], min_heap[j]
              j = l_index
            elif r_value<min_heap[j] and r_value<=l_value:
              min_heap[j], min_heap[r_index] = min_heap[r_index], min_heap[j]
              j = r_index
            else:
              break
      print min_heap
    return min_heap[0]


if __name__ == '__main__':
  a = Solution()
  # print a.findKthLargest([3,2,1,5,6,4], 2)
  print a.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
