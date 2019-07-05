"""
497. Random Point in Non-overlapping Rectangles (Medium)

Given a list of non-overlapping axis-aligned rectangles rects, write a function 
pick which randomly and uniformily picks an integer point in the space covered 
by the rectangles.

Note:

1. An integer point is a point that has integer coordinates. 
2. A point on the perimeter of a rectangle is included in the space covered by 
the rectangles. 
3. ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the 
integer coordinates of the bottom-left corner, and [x2, y2] are the 
integer coordinates of the top-right corner.
4. length and width of each rectangle does not exceed 2000.
5. 1 <= rects.length <= 100
6. pick return a point as an array of integer coordinates [p_x, p_y]
7. pick is called at most 10000 times.

Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output: 
[null,[4,1],[4,1],[3,3]]
Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]

Explanation of Input Syntax:

The input is two lists: the subroutines called and 
their arguments. Solution's constructor has one argument, the array of 
rectangles rects. pick has no arguments. Arguments are always wrapped with 
a list, even if there aren't any.

"""

import bisect
import random


class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.cdf = [0]
        self.data = rects
        for rect in self.data:
            x1, y1, x2, y2 = rect
            self.cdf.append(self.cdf[-1] + (x2-x1+1)*(y2-y1+1))
        self.cdf = self.cdf[1:]
        self.cdf = [item-1 for item in self.cdf]

    def pick(self):
        """
        :rtype: List[int]
        """
        rand = random.randint(0, self.cdf[-1])
        idx = bisect.bisect_left(self.cdf, rand)
        if idx > 0:
            diff = rand - self.cdf[idx-1]
        else:
            diff = rand
        # diff -> self.data[idx],
        x1, y1, x2, y2 = self.data[idx]
        y = y1 + diff // (x2-x1+1)
        x = x1 + diff % (x2-x1+1)
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

if __name__ == "__main__":
    a = Solution([[-2,-2,-1,-1],[1,0,3,0]])
    for _ in range(10):
        print(a.pick())