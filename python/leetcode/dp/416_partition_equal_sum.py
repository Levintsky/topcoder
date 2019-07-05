"""
416. Partition Equal Subset Sum (Medium)

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""

# Knapsack problem

class Solution(object):
  def canPartition(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    sum_nums = sum(nums)
    if sum_nums %2 == 1: return False
    sum_nums /= 2

    # dp init
    # matrix[i][j]: sum j can be done from nums[0..i]
    n_nums = len(nums)
    matrix = []
    for i in range(n_nums+1):
      matrix.append([True] + [False]*sum_nums)

    # dp
    for i in range(1, n_nums+1):
      for j in range(1, sum_nums+1):
        tmp = nums[i-1]
        if matrix[i-1][j] == True:
          matrix[i][j] = True
        elif j-tmp>=0 and matrix[i-1][j-tmp] == True:
          matrix[i][j] = True
    print matrix
    return matrix[-1][-1]


if __name__ == '__main__':
  a = Solution()
  print a.canPartition([1,5,11,5])
  print a.canPartition([2,3,5])
