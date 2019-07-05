# Back Tracking

## Partition Array
- Typical questions:
	- LC-473: Matchsticks to Square (Special case of 698, 4 partition)
    - Trick 0: greedy fit always ok? (fit 1 edge, safely remove, then fit the 2nd)
    - Trick 1: only need to fit 3 rather than 4?
	- LC-698: Partition to K Equal Sum Subsets
    - Greedy doesn't really work. counter example: [10,10,10,7,7,7,7,7,7,6,6,6], 3

## Traversal
- Typical questions:
	- LC-489: Robot Room Cleaner
	- **LC-488**: Zuma Game
  - LC-980: Unique Paths III

## Subsets, Permutations, Combination Sum, Palindrome Partitioning
- Subsets
	- LC-78: Subsets (input: distinct nums = [1,2,3], outputs: [[3], [1,2,3], ...])
  ```python
  def subsets(nums):
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
  ```

	- LC-90: Subsets II (same as 78, input nums can contain duplicates)
  ```python
  def subsetsWithDup(nums):
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
  ```

- Permutation:
	- LC-46: Permutations (**distinct**)
  ```python
  def permute(nums):
      result = []
      n = len(nums)

      def backtrack(tmpList):
          newList = [item for item in tmpList]
          result.append(newList)

          if len(tmpList) == n:
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
  ```

	- **LC-47**: Permutations II (with duplicates)
  ```python
  def permuteUnique(nums):
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
                  _ = tmpList.pop()
          return

      backtrack([])
      return result
  ```

- Combination Sum:
	- LC-39: Combination Sum
  ```python
  def combinationSum(nums, target):
      result = []
      nums.sort()
      n = len(nums)

      def backtrack(tmpList, remain, idx):
          if remain < 0:
              return
          elif remain == 0:
              newList = [item for item in tmpList]
              result.append(newList)
          else:
              for i in range(idx, n):
                  tmpList.append(nums[i])
                  backtrack(tmpList, remain-nums[i], i)
                  tmpList.pop()

      backtrack([], target, 0)
      return result
  ```

	- LC-40: Combination Sum II
  ```python
    def combinationSum2(self, nums, target):
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
  ```

- Palindrome:
	- LC-131: Palindrome Partitioning
  ```python
    def partition(s):
        result = []
        n = len(s)

        def backtrack(tmpList, start):
            if start == n:
                result.append([item for item in tmpList])
            else:
                for i in range(start, n):
                    if isPalin(s, low, i):
                        tmpList.append(s[low:i+1])
                        backtrack(tmpList, i+1)
                        _ = tmpList.pop()

        backtrack([], 0)
        return result
  ```