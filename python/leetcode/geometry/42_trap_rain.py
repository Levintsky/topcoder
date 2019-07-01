"""
42. Trapping Rain Water (Hard)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

"""
key point:
collect water by level
keep an active set (stack) of height starting from the highest so far;
for a new relative high height
collect the water between left high and current (which we can definitely collect)
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0: return 0
        result = 0
        stack = [(0, height[0])]
        for i in range(1, n):
            if height[i] < stack[-1][1]:
                stack.append((i, height[i]))
            else:
                while len(stack)>0 and stack[-1][1]<height[i]:
                    ind, h = stack.pop()
                    if len(stack) > 0:
                        result += (i-stack[-1][0]-1) * (min(height[i], stack[-1][1]) - h)
                        print(i, stack[-1][0], min(height[i], stack[-1][1]), h, result)
                        print('stack', stack)
                stack.append((i, height[i]))
            print('i', i, height[i], 'result', result, 'stack', stack)
        return result

    def solve2(self, height):
        n = len(height)
        stack = [] # keep a decreasing stack
        res = 0
        for i in range(n):
            if len(stack) == 0 or height[i] < stack[-1][1]:
                stack.append([i, height[i]])
            else:
                while len(stack) > 1 and height[i] > stack[-1][1]:
                    res += (i-stack[-2][0]-1)*(min(stack[-2][1], height[i])-stack[-1][1])
                    _ = stack.pop()
                if height[i] >= stack[-1][1]:
                    _ = stack.pop()
                stack.append([i, height[i]])
        return res

if __name__ == "__main__":
  a = Solution()
  print(a.solve2([0,1,0,2,1,0,1,3,2,1,2,1]))
  print(a.solve2([5,5,1,7,1,1,5,2,7,6]))
  # print a.trap([4,2,0,3,2,5])
