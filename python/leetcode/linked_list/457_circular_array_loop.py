"""
457. Circular Array Loop (Medium)

You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?
"""

"""
all indices as a set
for each item in the set, check:
  1. go until back to an visited item;
  2.a. if len of cycle == 1: false;
  2.b. elif re-visit the cycle if pos/neg iterates: fale;
  2.c. return True;
  3. return False;
"""


class Solution(object):
    def solve2(self, nums):
        n = len(nums)

        def getIndex(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue
            # slow/fast pointer
            j = i
            k = getIndex(i)
            # check same direction
            while nums[k] * nums[i] > 0 and nums[getIndex(k)] * nums[i] > 0:
                if j == k:
                    # check for loop with only one element
                    if j == getIndex(j):
                        break
                    return True
                j = getIndex(j)
                k = getIndex(getIndex(k))
            # loop not found, set all element along the way to 0
            j = i
            val = nums[i]
            while nums[j] * val > 0:
                next_ = getIndex(j)
                nums[j] = 0
                j = next_
        return False

    def circularArrayLoop(self, nums):
        len_ = len(nums)
        if len_ <= 1:
            return False

        set_ = set([i for i in range(len_)])
        result = [True] * len_  # record bad loops to avoid recomputation

        while len(set_) > 0:
            # randomly pop an item
            i = set_.pop()
            # start from i, go until
            ii = (i + nums[i]) % len_
            tmp_loop = [i, ii]
            while len(set_) > 0 and ii in set_:
                set_.remove(ii)
                ii = (ii + nums[ii]) % len_
                tmp_loop.append(ii)
            print(set_, ii)

            # now ii is the starting point of the loop
            flag = True
            if (ii + nums[ii]) % len_ == ii:
                # case 1: check loop-len == 1?
                flag = False
            elif result[ii] == False:
                # case 2: go to a previous known bad loop?
                flag = False
            else:
                # check +/- alternates
                pos_flag = nums[ii] > 0
                jj = (ii + nums[ii]) % len_
                while jj != ii:
                    if nums[jj] > 0 and not pos_flag:
                        flag = False
                        break
                    if nums[jj] < 0 and pos_flag:
                        flag = False
                        break
                    jj = (jj + nums[jj]) % len_
            if flag:
                return True
            else:
                for item in tmp_loop:
                    result[item] = False
        return False

    """
  def circularArrayLoop2(self, nums):
    n = len(nums)
    for i in range(n):
      if nums[i] == 0:
        continue
      else:
        if self.helper(nums, i):
          return True
    return False

  def helper(self, nums, start):
    n = len(nums)
    if n <= 1: return False
    print 'searching'
    # step 1: meet somewhere
    slow = (start + nums[start]) % n
    fast = (slow + nums[slow]) % n
    print slow, fast
    while slow != fast:
      slow = (slow + nums[slow]) % n
      fast = (fast + nums[fast]) % n
      fast = (fast + nums[fast]) % n
      print slow, fast
    # print slow, fast
    # step 2: beginning of the loop
    fast = start
    while slow != fast:
      slow = (slow + nums[slow]) % n
      fast = (fast + nums[fast]) % n
    print 'meeting: ', slow, fast

    # check 2 things:
    # 1. more than one element in the loop
    ret = True
    if slow == (slow+nums[slow])%n:
      # set eveything as zero along the line
      ret = False
    # print 'pass 1 element check'
    # 2. pure forward or backward
    forward_ = nums[slow]>0
    slow = (slow + nums[slow]) % n
    while slow != fast:
      tmp = nums[slow]
      if (forward_ and tmp<0) or (not forward_ and tmp>0):
        ret = False
        break
      slow = (slow + nums[slow]) % n
    # print 'pass pure forward/backward check'
    if not ret:
      # set everything along as zero
      slow = start
      while nums[slow] != 0:
        slow_next = (slow + nums[slow]) % n
        nums[slow] = 0
        slow = slow_next
    print nums
    return ret
  """


if __name__ == "__main__":
    a = Solution()
    print(a.circularArrayLoop([2, -1, 1, 2, 2]))
    print(a.circularArrayLoop([-1, 2]))
    print(a.circularArrayLoop([-2, 1, -1, -2, -2]))
    print(a.circularArrayLoop([2, 2, 2, 2, 2, 4, 7]))
    # print a.circularArrayLoop([3,1,2])
