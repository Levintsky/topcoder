'''
480. Sliding Window Median (Hard)

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.
'''
import collections

class MinHeap(object):
  def __init__(self, cmp=cmp):
    self.nums = []
    self.cnt = 0
    self.cmp = cmp

  def insert(self, num):
    self.nums.append(num)
    self.cnt += 1
    idx = self.cnt - 1
    self.sift_up(idx)

  def pop(self, num=0):
    self.nums[self.cnt-1], self.nums[0] = self.nums[0], self.nums[self.cnt-1]
    ret = self.nums[-1]
    self.nums = self.nums[:-1]
    self.cnt -= 1
    self.sift_down(0)
    return ret

  def sift_up(self, idx):
    # balance all the way up
    while idx>0:
      p_id = (idx-1) / 2
      if self.cmp(self.nums[p_id], self.nums[idx])>0:
        self.nums[p_id], self.nums[idx] = self.nums[idx], self.nums[p_id]
        idx = p_id
      else:
        break

  def sift_down(self, idx):
    while(idx<self.cnt):
      p_idx1 = 2*idx + 1
      p_idx2 = 2*idx + 2
      # print 'ids', idx, p_idx1, p_idx2
      # print self.nums[idx], self.nums[p_idx1], self.nums[p_idx2]
      swap_id, min_ = idx, self.nums[idx]
      if p_idx1 < self.cnt and self.cmp(self.nums[p_idx1], self.nums[idx])<0:
        swap_id, min_ = p_idx1, self.nums[p_idx1]
      if p_idx2 < self.cnt and self.cmp(self.nums[p_idx2], min_)<0:
        swap_id, min_ = p_idx2, self.nums[p_idx2]
      # print 'current, swap', idx, swap_id # , min_
      if swap_id == idx: break
      else:
        self.nums[swap_id], self.nums[idx] = self.nums[idx], self.nums[swap_id]
        idx = swap_id
      # print 'after swapping', self.nums

class HashHeap(object):
  def __init__(self, cmp=cmp):
    self.nums = []
    self.cnt = 0
    self.cmp = cmp
    self.loc = {}

  def insert(self, num):
    self.nums.append(num)
    self.cnt += 1
    idx = self.cnt - 1
    if num not in self.loc:
      self.loc[num] = set([idx])
    else:
      self.loc[num].add(idx)
    self.sift_up(idx)

  def swap(self, idx1, idx2):
    # swap the position of idx1, idx2
    n1, n2 = self.nums[idx1], self.nums[idx2]
    self.loc[n1].remove(idx1)
    self.loc[n2].remove(idx2)
    self.loc[n1].add(idx2)
    self.loc[n2].add(idx1)
    self.nums[idx1], self.nums[idx2] = self.nums[idx2], self.nums[idx1]

  def pop(self, num=0):
    self.swap(self.cnt-1, 0)
    # self.nums[self.cnt-1], self.nums[0] = self.nums[0], self.nums[self.cnt-1]
    ret = self.nums[-1]
    self.nums = self.nums[:-1]
    self.loc[ret].remove(self.cnt-1)
    self.cnt -= 1
    self.sift_down(0)
    return ret

  def sift_up(self, idx):
    if idx >= self.cnt: return
    # balance all the way up
    while idx>0:
      p_id = (idx-1) / 2
      if self.cmp(self.nums[p_id], self.nums[idx])>0:
        self.swap(p_id, idx)
        # self.nums[p_id], self.nums[idx] = self.nums[idx], self.nums[p_id]
        idx = p_id
      else:
        break

  def sift_down(self, idx):
    if idx >= self.cnt: return
    while(idx<self.cnt):
      p_idx1 = 2*idx + 1
      p_idx2 = 2*idx + 2
      # print 'ids', idx, p_idx1, p_idx2
      # print self.nums[idx], self.nums[p_idx1], self.nums[p_idx2]
      swap_id, min_ = idx, self.nums[idx]
      if p_idx1 < self.cnt and self.cmp(self.nums[p_idx1], self.nums[idx])<0:
        swap_id, min_ = p_idx1, self.nums[p_idx1]
      if p_idx2 < self.cnt and self.cmp(self.nums[p_idx2], min_)<0:
        swap_id, min_ = p_idx2, self.nums[p_idx2]
      # print 'current, swap', idx, swap_id # , min_
      if swap_id == idx: break
      else:
        self.swap(swap_id, idx)
        # self.nums[swap_id], self.nums[idx] = self.nums[idx], self.nums[swap_id]
        idx = swap_id
      # print 'after swapping', self.nums

  def remove(self, n):
    # remove n from the system
    # step 1: find a location, swap with cnt-1
    tmp_l = self.loc[n].pop()
    self.loc[n].add(tmp_l)
    if tmp_l != self.cnt-1:
      self.swap(tmp_l, self.cnt-1)

    # step 2: remove nums[cnt-1]
    self.loc[n].remove(self.cnt-1)
    self.nums = self.nums[:-1]
    self.cnt -= 1

    # step 3:
    self.sift_down(tmp_l)
    self.sift_up(tmp_l)

def test_heap():
  # a = MinHeap(cmp= lambda x1, x2: -cmp(x1,x2))
  a = HashHeap( cmp= lambda x1, x2: -cmp(x1,x2))
  for i in range(10, -1, -1):
    a.insert(i)
  for i in range(3):
    a.insert(5)
  print a.loc
  print a.nums[0]
  print a.nums[1:3]
  print a.nums[3:7]
  print a.nums[7:]
  # for i in range(10):
  print a.loc
  print 'removing'
  a.remove(5)
  # a.remove(7)
  # for i in range(7):
  #   print a.pop()
  print a.nums
  print a.loc
  '''print a.nums[0]
  print a.nums[1:3]
  print a.nums[3:7]
  print a.nums[7:]'''

class Solution(object):
  def solution2(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[float]
    """
    import bisect
    kls = nums[:k]
    kls.sort()
    def update(num1, num2):
      # remove num1, add num2 to kls
      id1 = bisect.bisect_left(kls, num1)
      del kls[id1]
      bisect.insort(kls, num2)

      if k%2 == 0:
        return sum(kls[k/2-1:k/2+1]) / 2.
      else:
        return float(kls[k/2])
    
    res = []
    # init
    if k % 2 == 0:
      res.append(sum(kls[k/2-1:k/2+1])/2.)
    else:
      res.append(float(kls[k/2])
    # iteration
    for i in range(len(nums)-k):
      res.append(update(nums[i], nums[i+k])
    return res

  def medianSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[float]
    """
    max_h = HashHeap(cmp= lambda x1, x2: -cmp(x1,x2)) # keep k/2 minimum
    min_h = HashHeap()
    result = []
    # init
    for i in range(k):
      max_h.insert(nums[i])
    for i in range(k/2):
      n = max_h.pop()
      min_h.insert(n)
    
    if k % 2 == 0:
      result.append((float(max_h.nums[0]) + float(min_h.nums[0]))/2.)
      for i in range(k, len(nums)):
        # add nums[i]
        if nums[i] <= max_h.nums[0]: max_h.insert(nums[i])
        else: min_h.insert(nums[i])

        # remove nums[i-k]
        if nums[i-k] <= max_h.nums[0]: max_h.remove(nums[i-k])
        else: min_h.remove(nums[i-k])
        # print 'step ', i, 'max_heap ', max_h.nums, 'min_heap', min_h.nums, 'result', result
        # print 'max_heap', max_h.loc
        # print 'min_heap', min_h.loc

        # balance if required
        # print 'max_heap', max_h.loc
        if len(max_h.nums) > len(min_h.nums):
          n = max_h.pop()
          min_h.insert(n)
        elif len(max_h.nums) < len(min_h.nums):
          n = min_h.pop()
          max_h.insert(n)
        result.append((float(max_h.nums[0]) + float(min_h.nums[0]))/2.)
        print 'step ', i, 'max_heap ', max_h.nums, 'min_heap', min_h.nums, 'result', result
        print 'max_heap', max_h.loc
        print 'min_heap', min_h.loc
    else:
      result.append(float(max_h.nums[0]))
      for i in range(k, len(nums)):
        # add nums[i]
        if nums[i] <= max_h.nums[0]: max_h.insert(nums[i])
        else: min_h.insert(nums[i])
        # remove nums[i-k]
        if nums[i-k] <= max_h.nums[0]: max_h.remove(nums[i-k])
        else: min_h.remove(nums[i-k])
        # balance if required
        # print 'max_heap', max_h.loc
        if len(max_h.nums) > (k+1)/2:
          n = max_h.pop()
          min_h.insert(n)
        elif len(max_h.nums) < (k+1)/2:
          n = min_h.pop()
          max_h.insert(n)
        result.append(float(max_h.nums[0]))
        # print 'step ', i, 'max_heap ', max_h.nums, 'min_heap', min_h.nums, 'result', result
        # print 'max_heap', max_h.loc
        # print 'min_heap', min_h.loc
    return result


if __name__ == '__main__':
  # test_heap()
  a = Solution()
  arr = [1,3,-1,-3,5,3,6,7]
  # arr = [2147483647,1,2,3,4,5,6,7,2147483647]
  print arr
  print a.medianSlidingWindow(arr, 4)
  # print a.medianSlidingWindow([1,4,2,3], 3)
  # print a.medianSlidingWindow([1,2], 2)
  
