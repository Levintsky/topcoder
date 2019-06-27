"""
84. Largest Rectangle in Histogram (Hard)

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

"""
Solution1: the jump trick

Solution2: O(n)
a stack to keep increasing order height
[(i1, h1), (i2, h2), ...]
for a new (i, h):
    case 1: h > h_max, directly append
    case 2: h = h_max, ignore
    case 3: h < h_max,
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0:
            return 0
        lessFromLeft = [0] * n
        lessFromRight = [0] * n
        lessFromRight[n - 1] = n
        lessFromLeft[0] = -1

        for i in range(1, n):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p

        for i in range(n - 2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = lessFromRight[p]
            lessFromRight[i] = p

        result = 0
        for i in range(n):
            result = max(result, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))
        return result

    def solution2(self, heights):
        heights.append(0)
        n = len(heights)
        stack = []
        maxArea = 0
        for i, item in enumerate(heights):
            while len(stack) > 0 and heights[stack[-1][0]] > item:
                idx, h = stack.pop()
                if len(stack) == 0:
                    w = i
                else:
                    w = i - 1 - stack[-1][0]
                maxArea = max(maxArea, h * w)
                print(maxArea)
            print(i, item, stack, maxArea)
            stack.append((i, item))
        return maxArea


if __name__ == "__main__":
    a = Solution()
    # print(a.largestRectangleArea([2,1,5,6,2,3]))
    print(a.solution2([3, 1, 1, 1]))
