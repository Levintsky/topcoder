"""
46. Permutations (Medium)

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        n = len(nums)

        def backtrack(tmpList):
            if len(tmpList) == n:
                newList = [item for item in tmpList]
                result.append(newList)
            else:
                for i in range(n):
                    if nums[i] in tmpList:
                        continue
                    else:
                        tmpList.append(nums[i])
                        backtrack(tmpList)
                        _ = tmpList.pop()
            return

        backtrack([])
        return result

    def solve2(self, nums):
        result = []
        n = len(nums)

        def generate(tmpList, i):
            # swap and add
            if i == n:
                newList = [item for item in tmpList]
                result.append(newList)

            for j in range(i, n): 
                tmpList[i], tmpList[j] = tmpList[j], tmpList[i]
                generate(tmpList, i+1)
                tmpList[i], tmpList[j] = tmpList[j], tmpList[i]

        generate(nums, 0)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.solve2([1,2,3]))