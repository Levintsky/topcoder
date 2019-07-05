"""
78. Subsets (Medium)

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        def backtrack(tmpList, idx):
            newList = [item for item in tmpList]
            result.add(newList)
            for i in range(idx, len(nums)):
                tmpList.append(nums[i])
                backtrack(tmpList, i+1)
                _ = tmpList.pop()
    
        backtrack([], 0)
        return result

    def solve2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        # nums.sort()

        for item in nums:
            new_result = []
            for tmpl in result:
                newl = [item2 for item2 in tmpl]
                newl.append(item)
                new_result.append(newl)
            result = result + new_result
        return result