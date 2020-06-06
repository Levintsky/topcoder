'''
307. Range Sum Query - Mutable (Medium)

Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

"""
Method 1: Segment Tree
# op1: Update: log(n)
# SegmentTreeNode
#   stard, end
#   left, right
#   val
# op2: Build_Tree()
# op3: Query_Sum()
  corner case: span the range (leaf node included)
  range all in left
  range all in right
  range in both left and right
"""

"""
Method 2: Binary Index Tree
for n numbers, create an array of size n+1
0 dummy node
1 [0,0] 2[0,1] 4[0,3] 8[0,7]
        3[2,2] 5[4,4]
**prefix tree**
a node 1010: 2**3 + 2**1
so start from 2**3, containing sum of next 2**1 numbers
then [0, n], start with node n+1, sum all numbers back to root
[m, n], sum(n+1) - sum(m)

Operation:
#1 update array[n], n+1 all the way to the end
  while i <= n:
    i += i & (-i)
  move the least significant 1 up, will always include array[i]
#2 Build tree:
#3 Get sum, all the way back to root
  while i >= 0:
    i -= i & (-i)
  remove the least significant 1
"""

class NumArray(object):
    # AC due to weak test cases, takes 1000ms
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.nums[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


class Seg_Tree_Node(object):
  def __init__(self, start, end, val):
    self.start = start
    self.end = end
    self.left = None
    self.right = None
    self.val = val


class NumArray2(object):
    # AC: faster with segment Tree
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [item for item in nums]
        self.nums.insert(0, 0)
        # build a segment tree
        self.root = self.build_tree(self.nums, 0, len(self.nums)-1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        print val, self.nums, i
        diff = val - self.nums[i+1]
        self.nums[i+1] = val
        node = self.root
        start, end = node.start, node.end
        # update everything along the line until start=end=i+1
        while(start!=end):
          node.val += diff
          mid = (start+end)/2
          if i+1 <= mid:
            end = mid
            node = node.left
          else:
            start = mid+1
            node = node.right
        node.val += diff

    def sumRange(self, i, j):
        """
        :type i: int
        :rtype: int
        """
        return self.helper_sum(i+1, j+1, self.root)

    def build_tree(self, nums, st, end):
       if st == end:
         root = Seg_Tree_Node(st, end, nums[st])
         return root
       # divide and conquer
       mid = (st+end)/2
       l_node = self.build_tree(nums, st, mid)
       r_node = self.build_tree(nums, mid+1, end)
       root = Seg_Tree_Node(st, end, l_node.val+r_node.val)
       root.left = l_node
       root.right = r_node
       return root

    def helper_sum(self, i, j, node):
       if i==node.start and j==node.end:
         return node.val
       mid = (node.start+node.end)/2
       if j <= mid:
         return self.helper_sum(i,j, node.left)
       elif i <= mid and j> mid:
         r_left = self.helper_sum(i, mid, node.left)
         r_right = self.helper_sum(mid+1, j, node.right)
         return r_left+r_right
       else:
         return self.helper_sum(i,j, node.right)


class NumArray3(object):
  def __init__(self, nums):
    """
    :type nums: List[int]
    """
    n = len(nums)
    self.nums = [item for item in nums]
    self.tree = [0] * (n+1)
    for i in range(n):
      self.helper(i, nums[i])    

  def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: void
    """
    v = val - self.nums[i]
    print 'diff', v
    self.helper(i, v)
    self.nums[i] += v

  def helper(self, i, v):
    n = len(self.nums)
    i += 1
    while i<=n:
      self.tree[i] += v
      i += i & (-i)

  def sumRange(self, i, j):
    """
    :type i: int
    :type j: int
    :rtype: int
    """
    sum_i = 0 # 0..i-1
    while i>0:
      sum_i += self.tree[i]
      i -= i & (-i)
    sum_j = 0
    j += 1
    while j>0:
      sum_j += self.tree[j]
      j -= j & (-j)
    return sum_j -sum_i

if __name__ == '__main__':
  # Building the structure
  nums = range(1,10)
  a = NumArray3(nums)
  # Try query sum
  'Query'
  for i in range(9):
    for j in range(i, 9):
      print i, j, a.sumRange(i, j), sum(nums[i:j+1])
      assert a.sumRange(i,j)==sum(nums[i:j+1])
  # update a val
  print a.tree
  nums[0] = 0
  a.update(0, 0)
  print a.tree
  # Try query sum
  'Query'
  for i in range(9):
    for j in range(i, 9):
      print i, j, a.sumRange(i, j), sum(nums[i:j+1])
      assert a.sumRange(i,j)==sum(nums[i:j+1])
  pass
  # nums = [2,1,1,3,2,3,4,5,6,7,8,9]
  # a = NumArray3(nums)
  # print a.tree
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
