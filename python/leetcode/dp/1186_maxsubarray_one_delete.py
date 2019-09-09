"""
1186. Maximum Subarray Sum with One Deletion (Medium)

Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

Example 1:

Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
Example 2:

Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
Example 3:

Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
 

Constraints:

1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
"""

class Solution(object):
    # wrong answer!
    # counter example...
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # case 1: all <= 0, return max
        if max(arr) <= 0:
            return max(arr)
        # case 2: all >= 0, return sum
        if min(arr) >= 0:
            return sum(arr)
        # case 3:
        arr = [item for item in arr if item != 0]
        curr, neg_min = arr[0], min(arr[0], 0)
        memo = []
        n = len(arr)
        for i in range(1, n):
            item = arr[i]
            if item * curr < 0:
                memo.append((curr, neg_min)) # end last one
                curr, neg_min = item, min(item, 0)
            else:
                curr += item
                neg_min = min(neg_min, item)
            if i == n-1:
                memo.append((curr, neg_min))
        res1 = max([item[0] for item in memo])
        res2 = 0
        for i in range(len(memo)-2):
            tmp = sum(memo[j][0] for j in range(i, i+3)) - memo[i+1][1]
            res2 = max(res2, tmp)
        return max(res1, res2)

    def solve2(self, arr):
        # case 1: all <= 0, return max
        if max(arr) <= 0:
            return max(arr)
        # case 2: all >= 0, return sum
        if min(arr) >= 0:
            return sum(arr)
        # dp
        best_ori = arr[0]
        best_del = 0
        result = 0
        for item in arr[1:]:
            new_ori = max(best_ori+item, item)

            new_del = max(best_del + item, best_ori)
            best_ori, best_del = new_ori, new_del
            result = max(result, best_ori, best_del)

            # print(best_ori, best_del)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.solve2([1,-2,0,3]))
    print(a.solve2([1,-2,-2,3]))
    print(a.solve2([-1,-1,-1,-1]))
    print(a.solve2([8,-1,6,-7,-4,5,-4,7,-6]))
    # print(a.maximumSum([1,-2,-2,3]))
    # print(a.maximumSum([-1,-1,-1,-1]))
