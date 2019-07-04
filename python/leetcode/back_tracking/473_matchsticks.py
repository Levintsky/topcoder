"""
473. Matchsticks to Square (Medium)

Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""

"""
According to https://en.wikipedia.org/wiki/Partition_problem, the partition problem (or number partitioning) is the task of deciding whether a given multiset S of positive integers can be partitioned into two subsets S1 and S2 such that the sum of the numbers in S1 equals the sum of the numbers in S2. The partition problem is NP-complete.

When I trying to think how to apply dynamic programming solution of above problem to this one (difference is divid S into 4 subsets), I took another look at the constraints of the problem:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

Sounds like the input will not be very large... Then why not just do DFS? In fact, DFS solution passed judges.

Anyone solved this problem by using DP? Please let me know :)

public class Solution {
    public boolean makesquare(int[] nums) {
      if (nums == null || nums.length < 4) return false;
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 4 != 0) return false;
        
      return dfs(nums, new int[4], 0, sum / 4);
    }
    
    private boolean dfs(int[] nums, int[] sums, int index, int target) {
      if (index == nums.length) {
          if (sums[0] == target && sums[1] == target && sums[2] == target) {
        return true;
          }
          return false;
      }
      
      for (int i = 0; i < 4; i++) {
          if (sums[i] + nums[index] > target) continue;
          sums[i] += nums[index];
            if (dfs(nums, sums, index + 1, target)) return true;
          sums[i] -= nums[index];
      }
      
      return false;
    }
}
Updates on 12/19/2016 Thanks @benjamin19890721 for pointing out a very good optimization: Sorting the input array DESC will make the DFS process run much faster. Reason behind this is we always try to put the next matchstick in the first subset. If there is no solution, trying a longer matchstick first will get to negative conclusion earlier. Following is the updated code. Runtime is improved from more than 1000ms to around 40ms. A big improvement.

public class Solution {
    public boolean makesquare(int[] nums) {
      if (nums == null || nums.length < 4) return false;
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 4 != 0) return false;
        
        Arrays.sort(nums);
        reverse(nums);
        
      return dfs(nums, new int[4], 0, sum / 4);
    }
    
    private boolean dfs(int[] nums, int[] sums, int index, int target) {
      if (index == nums.length) {
          if (sums[0] == target && sums[1] == target && sums[2] == target) {
        return true;
          }
          return false;
      }
      
      for (int i = 0; i < 4; i++) {
          if (sums[i] + nums[index] > target) continue;
          sums[i] += nums[index];
            if (dfs(nums, sums, index + 1, target)) return true;
          sums[i] -= nums[index];
      }
      
      return false;
    }
    
    private void reverse(int[] nums) {
        int i = 0, j = nums.length - 1;
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++; j--;
        }
    }
}
"""

import collections

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        target = sum(nums)
        if target % 4 != 0: return False
        target /= 4
        n = len(nums)
        sums = [0] * 4
        return self.helper(nums, sums, target, 0)

    def helper(self, nums, sums, target, index):
          n = len(nums)
          if n == index:
              if sums[0]==target and sums[1]==target and sums[2]==target: return True
              return False
          for i in range(4):
              if nums[index]+ sums[i]>target: continue
              sums[i] += nums[index]
              if self.helper(nums, sums, target, index+1): return True
              sums[i] -= nums[index]
          return False

    def solution2(self, nums):
        def dfs(nums, pos, target):
            if pos == len(nums): return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos+1, target): return True
                    target[i] += nums[pos]
            return False
        if len(nums) < 4: return False
        numSum = sum(nums)
        if numSum % 4 != 0: return False
        target = [numSum/4] * 4;
        return dfs(nums, 0, target)

    def solution3(self, nums):
        # AC, much faster, sorting in reverse order is very important
        def dfs(nums, pos, target):
            if pos == len(nums): return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos+1, target): return True
                    target[i] += nums[pos]
            return False
        if len(nums) < 4 : return False
        numSum = sum(nums)
        nums.sort(reverse=True)
        if numSum % 4 != 0: return False
        target = [numSum/4] * 4;
        return dfs(nums,0, target)

    def solve4(self, nums):
        def func(i, t):
            if t < 0: return False
            if not t: return True
            for j in range(i,n):
                if (j==i or nums[j]!=nums[j-1]):
                    ids.append(j)
                    if func(j+1,t-nums[j]): return True
                    ids.pop()
            return False

        s = sum(nums)
        if s % 4 or len(nums) < 4: return False
        s //= 4
        nums.sort(reverse=True)
        # trick 0: only need to fit 3 targets, 4th will automatically satisfy
        # greedy fit?
        for _ in range(3):
            # trick 1: always put the largest in
            ids, n = [0], len(nums)
            if func(1, s-nums[0]):
                for i in ids[::-1]:
                    nums.pop(i)
            else: return False
        return True

    def solve5(self, nums):
        n = len(nums)
        if n < 4: return False
        target = sum(nums)
        if target % 4: return False
        target //= 4
        nums.sort(reverse=True)

        visited = set()

        def func(idx, current_sum, cnt):
            # idx: starting id in nums
            # current_sum:
            # cnt: how many already satisfy?
            # return: bool
            if cnt == 3: return True

            if current_sum == target:
                return func(0, 0, cnt+1)

            if idx == len(nums): return False

            for i in range(idx, n):
                if i not in visited and current_sum + nums[i] <= target:
                    visited.add(i)
                    res = func(i+1, current_sum + nums[i], cnt)
                    if res: return True
                    visited.remove(i)
            return False

        # trick 0: only need to fit 3 targets, 4th will automatically satisfy
        result = func(0, 0, 0)
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.solve5([3,3,1,1,2,2,2,2]))
    # print(a.makesquare([1,1,2,2,2]))
    # print a.solution2([1,1,2,2,2])
    # print a.makesquare([3,3,3,3,4])
    # print(a.solution2([3,3,3,3,4]))
    # print a.solution3([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511])
    # print a.solution2([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511])
    # print a.makesquare([5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511])
