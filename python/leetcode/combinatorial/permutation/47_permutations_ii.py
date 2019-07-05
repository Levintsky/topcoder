"""

47. Permutations II (Medium)

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)
        used = [False] * n

        def backtrack(tmpList):
            if len(tmpList) == n:
                newList = [item for item in tmpList]
                result.append(newList)
            else:
                for i in range(n):
                    if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                        continue
                    used[i] = True
                    tmpList.append(nums[i])
                    backtrack(tmpList)
                    used[i] = False
                    _ = tmpList.pop()
            return
        
        backtrack([])
        return result

    def solve2(self, nums):
        ans  = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i < len(l) and l[i] == n:
                        break
            ans = new_ans
        return ans


if __name__ == "__main__":
    a = Solution()
    # print(a.permuteUnique([1,1,2]))
    print(a.solve2([1,1,2,2]))