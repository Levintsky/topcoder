'''
90. Subsets II (Medium)

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

import collections

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        def backtrack(tmpList, idx):
            newList = [item for item in tmpList]
            result.append(newList)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                tmpList.append(nums[i])
                backtrack(tmpList, i+1)
                _ = tmpList.pop()

        backtrack([], 0)
        return result

    def solve2(self, nums):
        memo = dict(collections.Counter(nums))
        klist = list(memo.keys())
        klist.sort()
        res = [[]]
        for k in klist:
            new_res = []
            for tmpList in result:
                for cnt in range(1, memo[k]+1):
                    newList = [item for item in tmpList]
                    newList = newList + [k] * cnt
                    new_res.append(newList)
            res += new_res
        return res

