"""
850. Rectangle Area II (Hard)

We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
"""

class Solution(object):
    def rectangleArea(self, rectangles):
        # All x showing up: i.e., x1 < x2 < ... < xn
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        # dict: {0: x0, 1: x1, ...}
        x_i = {v: i for i, v in enumerate(xs)}
        count = [0] * len(x_i)
        # sort by y value, mark enter and exit
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()
        # coverage
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            for i in range(x_i[x1], x_i[x2]):
                count[i] += sig
            cur_x_sum = sum(x2 - x1 if c else 0 for x1, x2, c in zip(xs, xs[1:], count))
        return area % (10 ** 9 + 7)

    def solve2(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # 1. All xs show up
        xs = set()
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
        xs = list(xs)
        xs.sort()
        memo_x = {}
        for i, item in enumerate(xs):
            memo_x[item] = i

        # 2. Sort by ys
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        L.sort()

        # 3. Area
        area = 0
        xs_val = []
        for i in range(len(xs)-1):
            xs_val.append(xs[i+1]-xs[i])
        xs_sig = [0] * len(xs_val) # current sign
        curr_y = L[0][0] # start with y0
        MOD = 10 ** 9 + 7
        for y, x1, x2, sig in L:
            # add area
            for val, tmp_sig in zip(xs_val, xs_sig):
                if tmp_sig > 0:
                    area = (area + (y-curr_y) * val) % MOD

            # update coverage
            ind1, ind2 = memo_x[x1], memo_x[x2]
            for i in range(ind1, ind2):
                xs_sig[i] += sig

            curr_y = y
        return area

    def solve3(self, rectangles):
        xs = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        st = NumArray(xs)
        L = []
        for x1, y1, x2, y2 in rectangles:
            L.append([y1, 1, x1, x2])
            L.append([y2, -1, x1, x2])
        L.sort()
        cur_y = cur_x_sum = area = 0
        for y, sig, x1, x2 in L:
            area += (y - cur_y) * cur_x_sum
            cur_y = y
            cur_x_sum = st.update(x1, x2, sig)
        return area % (10 ** 9 + 7)



if __name__ == "__main__":
    a = Solution()
    # print(a.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
    print(a.solve2([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))
    print(a.solve2([[0,0,1000000000,1000000000]]))
