"""
39. Combination Sum (Medium)

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        n = len(candidates)
        res = {0: [[0]*n]}
        for i in range(1, target+1):
            new_res = set()
            for idx, item in enumerate(candidates):
                if i - item in res:
                    for comb in res[i-item]:
                        list2_ = [item for item in comb]
                        list2_[idx] += 1
                        new_res.add(tuple(list2_))
            new_res = list(new_res)
            res[i] = new_res
        result = []
        for list_ in res[target]:
            tmp = []
            for i in range(n):
                if list_[i] > 0:
                    tmp += [candidates[i]] * list_[i]
            result.append(tmp)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.combinationSum([2,3,6,7], 7))
    print(a.combinationSum([2,3,5], 8))

