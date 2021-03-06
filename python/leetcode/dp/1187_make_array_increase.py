"""
1187. Make Array Strictly Increasing (Hard)

Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9
"""

import bisect, collections


class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # for i-th iteration, dp records possible values of arr1[i]
        # map possible vals to min-edit to get this val
        dp = {-1: 0}
        arr2.sort()
        for item in arr1:
            # tmp = collections.defaultdict(lambda: float('inf'))
            tmp = {}
            # (i+1)-th iteration, iterate through all possible i-th ending val
            for key in dp:
            	# if new added (i+1)-th item is larger than ith val, safe to add it
            	# update tmp[item] which uses item as the last val
                if item > key:
                    tmp[item] = min(tmp.get(item, float('inf')), dp[key])

                # use the smallest possible arr2[loc] as the (i+1)-th element
                # e.g. [1, 5]
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp.get(arr2[loc], float('inf')),dp[key]+1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1


if __name__ == "__main__":
	a = Solution()
	print(a.makeArrayIncreasing([1,5,3,6,7], [1,3,2,4]))
	print(a.makeArrayIncreasing([1,5,3,6,7], [1,3,4]))
	print(a.makeArrayIncreasing([1,5,3,6,7], [1,3,6]))
