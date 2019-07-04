"""
698. Partition to K Equal Sum Subsets (Medium)

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1: return True
        total = sum(nums)
        if total % k != 0: return False
        target = total / k
        sums = [0] * k
        nums.sort(reverse=True)
        result = self.helper(nums, sums, k, target, 0)
        return result

    def helper(self, nums, sums, k, target, index):
        n = len(nums)
        if n == index:
            for item in sums:
                if item != target: return False
            return True
        for i in range(k):
            if nums[index] + sums[i] > target:
                continue
            sums[i] += nums[index]
            if self.helper(nums, sums, k, target, index+1):
                return True
            sums[i] -= nums[index]
        return False

    def solve2(self, nums, k):
        # basic check
        n = len(nums)
        if n < k: return False
        sums = sum(nums)
        if sums % k != 0: return False
        target = sums // k

        nums.sort(reverse=True)
        ids = []

        def dfs(i, target):
            if target < 0:
                return False
            if target == 0:
                return True
            for ii in range(i, len(nums)):
                if ii == i or nums[ii] != nums[ii-1]:
                    ids.append(ii)
                    if dfs(ii+1, target-nums[ii]):
                        return True
                    ids.pop()
            return False

        for i in range(k-1):
            ids = [0]
            if not dfs(1, target-nums[0]):
                return False
            for id_ in ids[::-1]:
                nums.pop(id_)
        return True

    def solve3(self, nums, k):
        if sum(nums)%k != 0: return False
        target = sum(nums)//k
        #print(target)
        if max(nums) > target: return False
        
        nums.sort(key = lambda x: -x)
        
        visited = set()
        def search(index,temp_sum,count):
            #print(index,temp_sum,count)
            if count == k:
                return True
            if temp_sum == target:
                return search(0,0,count+1)
            if index == len(nums):
                return False
            if index not in visited and temp_sum+nums[index]<=target:
                visited.add(index)
                if search(index+1, temp_sum+nums[index], count):
                    return True
                visited.remove(index)
            return search(index+1, temp_sum,count)
            
        return search(0,0,0)

    def solve4(self, nums, k):
        n = len(nums)
        if n < k: return False
        target = sum(nums)
        if target % k: return False
        target //= k
        nums.sort(reverse=True)

        visited = set()

        def func(idx, current_sum, cnt):
            # idx: starting id in nums
            # current_sum:
            # cnt: how many already satisfy?
            # return: bool
            if cnt == k-1: return True

            if current_sum == target:
                if cnt == k-2:
                    return True
                for i, item in enumerate(nums):
                    if i not in visited:
                        visited.add(i)
                        res = func(i+1, item, cnt+1)
                        if res:
                            return True
                        else:
                            visited.remove(i)
                            return False

            if idx == len(nums): return False
            last_fail = target + 1
            for i in range(idx, n):
                if nums[i] == last_fail:
                    continue
                if i not in visited and current_sum + nums[i] <= target:
                    visited.add(i)
                    res = func(i+1, current_sum + nums[i], cnt)
                    if res:
                        return True
                    else:
                        last_fail = nums[i]
                    visited.remove(i)
            return False

        # trick 0: only need to fit 3 targets, 4th will automatically satisfy
        result = func(0, 0, 0)
        return result


if __name__ == "__main__":
    a = Solution()
    # arr = [7628,3147,7137,2578,7742,2746,4264,7704,9532,9679,8963,3223,2133,7792,5911,3979]
    # k = 6
    # print a.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
    # print a.canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5)
    # print(a.canPartitionKSubsets(arr, 6))
    # arr = [10,10,10,7,7,7,7,7,7,6,6,6]
    # arr = [10,10,10,7,7,7,7,7,7,6,6,6]
    # print(a.solve4(arr, 3))
    arr = [1,1,1,1,1,1]
    print(a.solve4(arr, 3))
