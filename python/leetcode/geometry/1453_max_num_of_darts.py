"""
1453. Maximum Number of Darts Inside of a Circular Dartboard (Hard)

You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of points on a 2D plane. 

Return the maximum number of points that are within or lie on any circular dartboard of radius r.

Example 1:

Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
Output: 4
Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all points.
Example 2:



Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
Example 3:

Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
Output: 1
Example 4:

Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
Output: 4
 

Constraints:

1 <= points.length <= 100
points[i].length == 2
-10^4 <= points[i][0], points[i][1] <= 10^4
1 <= r <= 5000
"""

"""
Reference
POJ: http://poj.org/problem?id=1981
StackOverflow: https://stackoverflow.com/questions/3229459/algorithm-to-cover-maximal-number-of-points-with-one-circle-of-given-radius/3229582#3229582


Plan
Well, I doubt if this problem is appropriate for Leetcode or interview.

If you meet this prolem during interview,
you can ask the interviewer:
"Could you give me some APIs?"


Explanation
The basic idea is that,
imagine that we are shrink the final circle,
until there are at least 2 points on the circle.

We can enumerate all possible circles based on the given points.


Solution 1: O(N^4) brute force
Enumerate all combinations of 3 points,
find the circumcenter of these 3 points.

Use this circumcenter as the center of circle,
and count how many points inside.

If the result >=3, we won't miss it during this search.

Time O(N^4)
Space O(1)


Solution 2:
Enumerate all combinations of 2 points,
find the circle going through them with radius = r.

Use this circumcenter as the center of circle,
and count how many points inside.

Also explained by Alexandre C:
Basic observations :

I assume the radius is one,
since it doesn't change anything.
given any two points,
there exists at most two unit circles on which they lie.
given a solution circle to your problem,
you can move it until it contains two points of your set
while keeping the same number of points of your set inside it.
The algorithm is then:

For each pair of points,
if their distance is < 2,
compute the two unit circles C1 and C2 that pass through them.
Compute the number of points of your set inside C1 and C2
Take the max.
Time O(N^3)
Space O(1)

Python

    def numPoints(self, A, r):
        res = 1
        for (x1, y1), (x2, y2) in itertools.combinations(A, 2):
            d = ((x1 - x2)**2 + (y1 - y2)**2) / 4.0
            if d > r * r: continue
            x0 = (x1 + x2) / 2.0 + (y2 - y1) * (r * r - d)**0.5 / (d * 4) ** 0.5
            y0 = (y1 + y2) / 2.0 - (x2 - x1) * (r * r - d)**0.5 / (d * 4) ** 0.5
            res = max(res, sum((x - x0)**2 + (y - y0)**2 <= r * r + 0.00001 for x, y in A))

            x0 = (x1 + x2) / 2.0 - (y2 - y1) * (r * r - d)**0.5
            y0 = (y1 + y2) / 2.0 + (x2 - x1) * (r * r - d)**0.5
            res = max(res, sum((x - x0)**2 + (y - y0)**2 <= r * r + 0.00001 for x, y in A))
        return res
Solution 3
Enumerate points,
and draw a circle with radius = r * 2
Find the maximum overlapped circle arc.
(Don't really know how to explain it,
please refer to the original problem)

Time O(N^2logN)
Space O(1)
"""

"""
Algo
Pick a point, say P, from the set, and rotate a circle with fixed-radius r. During the rotation P lies on the circumference of the circle (note P is not the center) and maintain a count of the number of points in the circle at an angle Θ (between PC and x-axis, where C is the center of the circle).

For every other point Q within 2*r distance to P, compute the angle Θ when Q enters the circle and the angle Θ when Q exits the circle with math. Sort the angles and scan through it to check the maximum points in the circle.

Perform the above operation for all points to find the maximum.

Implementation (time complexity O(N^2 logN) | space complexity O(N))

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        ans = 1
        for x, y in points: 
            angles = []
            for x1, y1 in points: 
                if (x1 != x or y1 != y) and (d:=sqrt((x1-x)**2 + (y1-y)**2)) <= 2*r: 
                    angle = atan2(y1-y, x1-x)
                    delta = acos(d/(2*r))
                    angles.append((angle-delta, +1)) #entry
                    angles.append((angle+delta, -1)) #exit
            angles.sort(key=lambda x: (x[0], -x[1]))
            val = 1
            for _, entry in angles: 
                ans = max(ans, val := val+entry)
        return ans 
"""

import math

class Solution(object):
    def numPoints(self, points, r):
        """
        :type points: List[List[int]]
        :type r: int
        :rtype: int
        """
        def distance(p1, p2):
            s = 0.
            for i in [0, 1]:
                s += (p1[i] - p2[i]) ** 2
            return math.sqrt(s)

        def count_inlier(p):
            s = [(item[0]-p[0])**2 + (item[1]-p[1])**2 for item in points]
            res = 0
            for item in s:
                if item < r ** 2 + 0.00001:
                    res += 1
            return res


        result = 1
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                # distance
                xi, yi = points[i]
                xj, yj = points[j]
                dist = (xi-xj) ** 2 + (yi-yj) ** 2
                if dist > 4 * r * r:
                    continue
                midi, midj = (xi+xj)/2., (yi+yj)/2.
                dist_left = math.sqrt(r ** 2 - dist / 4.)

                dir_ = yj-yi, xi-xj
                norm = math.sqrt(dir_[0] ** 2 + dir_[1] ** 2)
                dir_ = dir_[0]/norm, dir_[1]/norm

                pot1 = midi+dir_[0]*dist_left, midj+dir_[1]*dist_left
                pot2 = midi-dir_[0]*dist_left, midj-dir_[1]*dist_left

                tmpres = count_inlier(pot1)
                result = max(result, tmpres)
                tmpres = count_inlier(pot2)
                result = max(result, tmpres)
                if result == n:
                    return n

        return result


if __name__ == "__main__":
    a = Solution()
    # print(a.numPoints([[-2,0],[2,0],[0,2],[0,-2]], 2))
    print(a.numPoints([[-2,0],[2,0],[0,2],[0,-2]], r = 2))
    print(a.numPoints([[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], 5))
    print(a.numPoints([[-2,0],[2,0],[0,2],[0,-2]], r = 1))
    print(a.numPoints([[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2))
