"""
1037. Valid Boomerang (Easy)

A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false

Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
"""

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # check distinct
        set_ = set()
        for x, y in points:
            set_.add((x, y))
        if len(set_) < 3: return False
        # check in a line
        dx1 = points[0][0] - points[1][0]
        dy1 = points[0][1] - points[1][1]
        dx2 = points[0][0] - points[2][0]
        dy2 = points[0][1] - points[2][1]
        if dx1 * dy2 == dy1 * dx2:
        	return False
        else:
        	return True


if __name__ == "__main__":
	a = Solution()
	print(a.isBoomerang([[1,1],[2,3],[3,2]]))
	print(a.isBoomerang([[1,1],[2,2],[3,3]]))