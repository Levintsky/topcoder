"""
939. Minimum Area Rectangle (Medium)

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = -1

        memo = set()
        for x, y in points:
            memo.add((x,y))
        
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in memo and (x2, y1) in memo:
                    tmp = abs(x1-x2) * abs(y1-y2)
                    res = min(res, tmp)
        if res < float('inf'):
            return res
        else:
            return 0

    def solve(self, points):
        # Better, faster
        seen = set()
        res = float('inf')
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < res:
                        res = area
            seen.add((x1, y1))
        return res if res < float('inf') else 0

"""
Another idea is that,
For each x value in sorted order, check all y pairs.

In most cases, all points randomly distribute.
Only 500 points in 40001 * 40001 possible coordinates.
No two points will have the same x value or y value.
There will be no rectangle and the result is 0.
This will be O(N) solution.

However, it seems that, in the test cases, it has a really big amount of rectangles.
In these worst cases, the time complexity is O(nx * nx * ny) < O(N ^ 1.5).

In the extreme worst cases, like all points have x = 0 or y = 0
Time complexity will be O(N^2)

O(N^1.5), 80ms

    def minAreaRect(self, points):
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0
"""
