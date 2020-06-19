"""
963. Minimum Area Rectangle II (Medium)


Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:



Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:



Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:



Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
 

Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
"""

import math


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        memo = {} # diagonal, mid to point
        
        for i in range(n):
            for j in range(i+1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                key = (xi-xj) ** 2 + (yi-yj) ** 2, xi + xj, yi + yj
                if key not in memo:
                    memo[key] = []
                memo[key].append((i, j))
                
        best = None
        for k, l in memo.items():
            n = len(l)
            for i in range(n):
                for j in range(i+1, n):
                    ind1, ind2 = l[i]
                    ind3, ind4 = l[j]
                    x1, y1 = points[ind1]
                    x2, y2 = points[ind2]
                    x3, y3 = points[ind3]
                    dist1 = math.sqrt((x1-x3) ** 2 + (y1-y3) ** 2)
                    dist2 = math.sqrt((x2-x3) ** 2 + (y2-y3) ** 2)
                    if best is None:
                        best = dist1 * dist2
                    else:
                        best = min(best, dist1 * dist2)
        if best is None:
            return 0.
        else:
            return best


if __name__ == "__main__":
    a = Solution()
    print(a.minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]))
    print(a.minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]]))
    print(a.minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]]))
    print(a.minAreaFreeRect([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]))
