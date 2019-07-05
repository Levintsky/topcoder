"""
40. Combination Sum II (Medium)

Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)

        def backtrack(tmpList, remain, idx):
            if remain == 0:
                newList = [item for item in tmpList]
                result.append(newList)
            else:
                for i in range(idx, n):
                    if i != idx and nums[i] == nums[i-1]:
                        continue
                    if nums[i] > remain:
                        return
                    tmpList.append(nums[i])
                    backtrack(tmpList, remain-nums[i], i+1)
                    tmpList.pop()

        backtrack([], target, 0)
        return result

    def solve2(self, candidates, target):
        candidates.sort()
        self.res = []
        self.helper(candidates, target, [])
        return self.res
        
    def helper(self, candidates, target, cur):
        if target == 0:
            self.res.append(cur)
            return
        for i in range(len(candidates)):
            if i != 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] <= target:
                self.helper(candidates[i+1:], target-candidates[i], cur + [candidates[i]])
            else:
                break

if __name__ == "__main__":
    a = Solution()
    # print(a.combinationSum2([10,1,2,7,6,1,5], 8))
    # print(a.combinationSum2([2,5,2,1,2], 5))
    # print(a.combinationSum2([3,1,3,5,1,1], 8))
    arr = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
    print(a.combinationSum2(arr, 27))
