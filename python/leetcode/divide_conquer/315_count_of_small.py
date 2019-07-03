'''
315. Count of Smaller Numbers After Self (Hard)

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''

"""
Solution 1: BST (from back to front)
Every node will maintain a val sum recording the total of number on it's left bottom side, dup counts the duplication. For example, [3, 2, 2, 6, 1], from back to beginning,we would have:

                1(0, 1)
                     \
                     6(3, 1)
                     /
                   2(0, 2)
                       \
                        3(0, 1)
When we try to insert a number, the total number of smaller number would be adding dup and sum of the nodes where we turn right.
for example, if we insert 5, it should be inserted on the way down to the right of 3, the nodes where we turn right is 1(0,1), 2,(0,2), 3(0,1), so the answer should be (0 + 1)+(0 + 2)+ (0 + 1) = 4

if we insert 7, the right-turning nodes are 1(0,1), 6(3,1), so answer should be (0 + 1) + (3 + 1) = 5

public class Solution {
    class Node {
        Node left, right;
        int val, sum, dup = 1;
        public Node(int v, int s) {
            val = v;
            sum = s;
        }
    }
    public List<Integer> countSmaller(int[] nums) {
        Integer[] ans = new Integer[nums.length];
        Node root = null;
        for (int i = nums.length - 1; i >= 0; i--) {
            root = insert(nums[i], root, ans, i, 0);
        }
        return Arrays.asList(ans);
    }
    private Node insert(int num, Node node, Integer[] ans, int i, int preSum) {
        if (node == null) {
            node = new Node(num, 0);
            ans[i] = preSum;
        } else if (node.val == num) {
            node.dup++;
            ans[i] = preSum + node.sum;
        } else if (node.val > num) {
            node.sum++;
            node.left = insert(num, node.left, ans, i, preSum);
        } else {
            node.right = insert(num, node.right, ans, i, preSum + node.dup + node.sum);
        }
        return node;
    }
}
"""

"""
Solution 2:
The smaller numbers on the right of a number are exactly those that jump from its right to its left during a stable sort. So I do mergesort with added tracking of those right-to-left jumps.

Update, new version

def countSmaller(self, nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller
"""

import bisect

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.cnt = 0
        # record number of nodes on the left
        self.dup = 1
        self.left = None
        self.right = None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = nums[::-1]
        if len(nums) == 0: return False
        result = [0]
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
          tmp = self.find(root, nums[i], 0)
          result.append(tmp)
        result = result[::-1]
        print(root.val, root.cnt, root.dup)
        return result

    def find(self, node, num, cnt):
        if node.val == num:
            node.dup += 1
            return cnt + node.cnt
        elif num > node.val: # inserted number is larger than node value
            cnt += node.cnt + node.dup
            if node.right is not None:
                return self.find(node.right, num, cnt)
            else:
                new_node = TreeNode(num)
                node.right = new_node
                return cnt
        else: # inserted number is smaller than node value
            node.cnt += 1
            if node.left is not None:
                return self.find(node.left, num, cnt)
            else:
                new_node = TreeNode(num)
                node.left = new_node
                return cnt

    def solve2(self, nums):
      n = len(nums)
      if n == 0: return []
      nums_ = zip(range(n), nums)
      def sort_(enums_):
          if len(enums_) < 2:
              return enums_
          half = len(enums_)/2
          left, right = sort_(enums_[:half]), sort_(enums_[half:])
          i, j = 0, 0
          m, n = len(left), len(right)
          while i < m or j < n:
              if j == n or (i < m and left[i][1] <= right[j][1]):
                  enums_[i+j] = left[i]
                  smaller[left[i][0]] += j
                  i += 1
              else:
                  enums_[i+j] = right[j]
                  j += 1
          return enums_
      smaller = [0] * n
      sort_(nums_)
      return smaller

    def solve3(self, nums):
        result = []
        tmp = []
        n = len(nums)
        for i in range(n-1, -1, -1):
            item = nums[i]
            idx = bisect.bisect_left(tmp, item)
            result.append(idx)
            bisect.insort(tmp, item)
        return result[::-1]


if __name__ == "__main__":
    a = Solution()
    # print(a.countSmaller([6,0,3,2,2,6,1]))
    # print(a.solve2([3,2,2,6,1]))
    print(a.solve3([5,2,6,1]))
    print(a.solve3([6,0,3,2,2,6,1]))
