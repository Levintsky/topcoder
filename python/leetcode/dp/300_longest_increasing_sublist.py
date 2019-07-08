'''
300. Longest Increasing Subsequence (Medium)

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      # AC, old version
      n = len(nums)
      if n <= 1:
          return n
      # minimum last number 
      result = [nums[0]]
      for i in range(1, n):
          item = nums[i]
          # change the while loop to binary-search
          # we can get O(nlogn)
          j = len(result) -1 
          while(j>=0):
            # append a new one if possible
            if item > result[-1]:
                result.append(item)
            if j==0:
                result[0] = min(result[0], item)
            elif item>result[j-1] and item<result[j]:
                result[j] = item
            j -= 1
          print(i, result)
      return len(result)

    def solve2(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      # AC, new version, much faster
      n = len(nums)
      if n <= 1: return n
      best_seq = [nums[0]]
      curr_seq = [nums[0]]
      i = 1
      while i<n:
          if nums[i] > best_seq[-1]: best_seq.append(nums[i])

          if nums[i] > curr_seq[-1]: curr_seq.append(nums[i])
          else:
              while len(curr_seq)>0 and curr_seq[-1]>=nums[i]:
                  curr_seq.pop()
              curr_seq.append(nums[i])
          if (len(curr_seq)>len(best_seq)) or (len(curr_seq)==len(best_seq) and curr_seq[-1]<best_seq[-1]):
              best_seq = [item for item in curr_seq]
          i += 1
          print(best_seq, curr_seq)
      return len(best_seq)

    def solve3(self, nums):
        n = len(nums)
        if n <= 1: return n
        result = [0] * n
        result[0] = nums[0]
        cnt = 1
        for item in nums:
            idx = self.bsearch(result, cnt, item)
            if idx == cnt:
                cnt += 1
                result[idx] = item
            elif result[idx] > item:
                result[idx] = item
            print(result, idx, item)
        return cnt

    def bsearch(self, nums, len_, val):
        print('search in: ', val, nums[:len_])
        if val > nums[len_-1]: return len_
        # find first num >= val
        start = 0
        end = len_
        mid = (start + end) // 2
        while start < end:
            mid = (start + end) // 2 
            if nums[mid] == val: return mid
            elif nums[mid] < val:
                start = mid + 1
            else: # nums[mid] > val
                end = mid
        mid = min(len_-1, max(start, end))
        if nums[mid] >= val:
            return mid
        else:
            return mid+1

    def solve4(self, nums):
        inc = []
        for item in nums:
            ind = bisect.bisect_left(inc, item)
            if ind == len(inc):
                inc.append(item)
            else:
                inc[ind] = item
        return len(inc)

if __name__ == '__main__':
    a = Solution()
    print(a.solve3([10, 9, 2, 5, 3, 7, 101, 18]))
    print(a.solve4([10, 9, 2, 5, 3, 7, 101, 18]))
    print(a.solve3([10, 9, 2, 5, 3, 4]))
    print(a.solve4([10, 9, 2, 5, 3, 4]))
