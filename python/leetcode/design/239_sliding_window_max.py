"""
239. Sliding Window Maximum (Hard)

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

"""
Solution 1:
We scan the array from 0 to n-1, keep "promising" elements in the deque. The algorithm is amortized O(n) as each element is put and polled once.

At each i, we keep "promising" elements, which are potentially max number in window [i-(k-1),i] or any subsequent window. This means

If an element in the deque and it is out of i-(k-1), we discard them. We just need to poll from the head, as we are using a deque and elements are ordered as the sequence in the array

Now only those elements within [i-(k-1),i] are in the deque. We then discard elements smaller than a[i] from the tail. This is because if a[x] <a[i] and x<i, then a[x] has no chance to be the "max" in [i-(k-1),i], or any other subsequent window: a[i] would always be a better candidate.

As a result elements in the deque are ordered in both sequence in array and their value. At each step the head of the deque is the max element in [i-(k-1),i]

More thought:
the queue is always a decreasing sequence.
"""

"""
Solution 2:

For Example: A = [2,1,3,4,6,3,8,9,10,12,56], w=4

partition the array in blocks of size w=4. The last block may have less then w.
2, 1, 3, 4 | 6, 3, 8, 9 | 10, 12, 56|

Traverse the list from start to end and calculate max_so_far. Reset max after each block boundary (of w elements).
left_max[] = 2, 2, 3, 4 | 6, 6, 8, 9 | 10, 12, 56

Similarly calculate max in future by traversing from end to start.
right_max[] = 4, 4, 4, 4 | 9, 9, 9, 9 | 56, 56, 56

now, sliding max at each position i in current window, sliding-max(i) = max{right_max(i), left_max(i+w-1)}
sliding_max = 4, 6, 6, 8, 9, 10, 12, 56
"""

import collections


class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums) == 0: return []
    q = collections.deque()
    # init
    for i in range(k):
      while len(q)>0 and q[-1]<nums[i]:
        q.pop()
      q.append(nums[i])
    result = [q[0]]
    # go through
    for i in range(k, len(nums)):
      # remove nums[i-(k-1)]
      if q[0] == nums[i-k]:
        q.popleft()
      # add nums[i]
      while len(q)>0 and q[-1]<nums[i]:
        q.pop()
      q.append(nums[i])
      result.append(q[0])
    return result


if __name__ == '__main__':
  a = Solution()
  print a.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
