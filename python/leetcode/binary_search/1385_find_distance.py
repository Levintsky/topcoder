"""
1385. Find the Distance Value Between Two Arrays (Easy)

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2

Example 2:
Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Example 3:
Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1

Constraints:

1 <= arr1.length, arr2.length <= 500
-10^3 <= arr1[i], arr2[j] <= 10^3
0 <= d <= 100
"""

import bisect


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        cnt = 0
        for item in arr1:
            if item < arr2[0] - d or item > arr2[-1] + d:
                cnt += 1
                continue
            else:
                # find the first idx s.t. arr2[idx] > d 
                idx = bisect.bisect(arr2, item)
                if idx < len(arr2) and arr2[idx] <= item + d:
                    continue
                elif idx > 0 and arr2[idx-1] >= item - d:
                    continue
                cnt += 1
        return cnt


if __name__ == "__main__":
    a = Solution()
    print(a.findTheDistanceValue([4,5,8], [10,9,1,8], 2))
    print(a.findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3))
    print(a.findTheDistanceValue([2,1,100,3], [-5,-2,10,-3,7], 6))
