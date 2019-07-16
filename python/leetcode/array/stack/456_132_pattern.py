"""
456. 132 Pattern (Medium)

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

"""
new idea:
# in a 132 pattern
# find "3" first (suppose nums[i])
# left pass: min until this number
# right pass: max until nums[i] from right?
  still need a stack to do that in linear time
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = nums[::-1]
        n = len(nums)
        if n <= 2:
            return False
        # find 231 pattern
        n2 = []
        n3 = min(nums) - 1

        i = 0
        while i < n:
            if nums[i] < n3:
                return True
            else:
                # pop too small things out
                while len(n2) > 0 and nums[i] > n2[-1]:
                    n3 = n2[-1]
                    n2.pop()
                n2.append(nums[i])
            # print 'step: ', i, 'n2', n2, 'n3', n3, 'current', nums[i]
            i += 1
        return False

    def solution2(self, nums):
        # s1, s2, s3 in order, s.t. s1 < s3 < s2
        s3 = min(nums) - 1  # imagine there is super small s3 appended at the end
        stack = []  # stack saves potential s3 in decreasing order
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while len(stack) > 0 and nums[i] > stack[-1]:
                    s3 = stack.pop()
            stack.append(nums[i])
            print(i, nums, stack, s3)
        return False


if __name__ == "__main__":
    a = Solution()
    """print a.find132pattern([-2,1,2,-2,1,2])
  print a.find132pattern([1,2,3,4]) # False
  print a.find132pattern([3,1,4,2]) # True
  print a.find132pattern([-1,3,2,0]) # True
  print a.find132pattern([1,0,1,-4,-3]) # False
  print a.find132pattern([3,5,0,3,4]) # True"""
    # print a.find132pattern([10,12,6,8,3,11]) # True
    # print a.find132pattern([-2, 1, 1, -2, 1, 1]) # False
    # print a.find132pattern([2, 4, 3, 1]) # True
    print(a.solution2([3, 5, 0, 2, 4]))
