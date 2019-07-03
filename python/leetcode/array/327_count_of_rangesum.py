'''
327. Count of Range Sum (Hard)

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i <= j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
'''

import bisect


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
      """
      :type nums: List[int]
      :type lower: int
      :type upper: int
      :rtype: int
      """
      n = len(nums)
      if n == 0: return 0
      # step 1: pre-process the sums
      sums = [0]
      for i in range(n):
        sums.append(sums[-1] + nums[i])
      print(sums)

      # step 2: merge-sort
      self.stat = 0
      self.merge_sort(sums, 0, len(sums)-1, lower, upper)
      return self.stat

    def merge_sort(self, nums, begin, end, lower, upper):
      if begin >= end:
        return
      # [begin, mid], [mid+1, end]
      mid = (begin + end) / 2
      self.merge_sort(nums, begin, mid, lower, upper)
      self.merge_sort(nums, mid+1, end, lower, upper)

      # stat
      i = begin
      j = mid+1
      k = mid+1
      while i <= mid:
        while j <= end and nums[j]-nums[i] < lower:
          j += 1
        k = j
        while k <= end and nums[k]-nums[i] <= upper:
          k += 1
        # print nums[k]-nums[i]
        self.stat += (k-j)
        i += 1
      # merge
      tmp = []
      i = begin
      j = mid+1
      while i <= mid or j <= end:
        if j > end or (i<=mid and nums[i]<nums[j]):
          tmp.append(nums[i])
          i += 1
        else:
          tmp.append(nums[j])
          j += 1
      nums[begin:end+1] = tmp
      return

    def solve2(self, nums, lower, upper):
        curr = [0]
        sort_cur = [0]
        result = 0
        for i, item in enumerate(nums):
            curr.append(curr[-1] + item)
            # insert
            tmp = curr[-1]
            # search how many >= tmp-upper
            idx1 = bisect.bisect_left(sort_cur, tmp-upper)
            cnt1 = i + 1 - idx1          
            idx2 = bisect.bisect(sort_cur, tmp-lower)
            cnt2 = i + 1 - idx2
            result += cnt1 - cnt2
            bisect.insort(sort_cur, tmp)
        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.countRangeSum([-2, 5, -1], -2, 2))
    print(a.solve2([-2,5,-1],-2,2))
    print(a.solve2([-1,1], 0, 0))
