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

    def solve2(self, nums, target):
        result = []
        nums.sort()
        n = len(nums)

        def backtrack(tmpList, remain, idx):
            if remain < 0:
                return
            elif remain == 0:
                # newList = [item for item in tmpList]
                # result.append(newList)
                result.append(tmpList)
            else:
                for i in range(idx, n):
                    # tmpList.append(nums[i])
                    backtrack(tmpList + [nums[i]], remain-nums[i], i)
                    # tmpList.pop()

        backtrack([], target, 0)
        return result

    def solve3(self, nums, target):
        res=[]
        nums.sort()
        def dfs(remain,stack):
            if remain==0:
                res.append(stack)
                
            for item in nums:
                if item > remain:
                    break
                if stack and item>stack[-1]:
                    print('here', stack, item)
                    continue
                else:
                    dfs(remain-item,stack+[item])
        dfs(target,[])
        return res


if __name__ == "__main__":
    a = Solution()
    # print(a.combinationSum([2,3,6,7], 7))
    # print(a.combinationSum([2,3,5], 8))
    print(a.solve2([2,3,6,7], 7))
