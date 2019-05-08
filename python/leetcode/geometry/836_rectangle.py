"""
836. Rectangle Overlap (Easy)

A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
"""

"""
check problem 223
"""

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        left = max(x1, x3)
        right = max(min(x2, x4), left)

        up = max(y1, y3)
        down = max(min(y2, y4), up)
        return (right-left) * (down-up) > 0:


if __name__ == "__main__":
    a = Solution()
    print(a.isRectangleOverlap([0,0,2,2], [1,1,3,3]))
    print(a.isRectangleOverlap([0,0,1,1], [1,0,2,1]))
