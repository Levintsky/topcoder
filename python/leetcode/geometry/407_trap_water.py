"""
407. Trapping Rain Water II (Hard)

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
"""

"""
Solution 1:
https://leetcode.com/problems/trapping-rain-water-ii/discuss/89467/Why-reinvent-the-wheel-An-easy-understood-commented-solution-based-on-trapping-rain-1

Basic physics:
Unlike bricks, water flows to wherever it could. 
i.e we can't have the follwoing config made with water, but can do it with bricks
000
010
000
In the case above, if the "1" is built with water, that water can't stay. It needs to be spilled!

2 steps Algorithm: 
1. Since we know how to trap rain water in 1d, we can just transfor this 2D problem into 2 1D problems
    we go row by row, to calculate each spot's water
    we go column by column, to calculate each spot's water

2. Then, here comes the meat,
    For every spot that gets wet, from either row or column calculation, the water can possibly spill.
    We need to check the water height aganist it's 4 neighbors. 
        If the water height is taller than any one of its 4 neightbors, we need to spill the extra water.
        If we spill any water from any slot, then its 4 neightbors needs to check themselves again.
            For example, if we spill some water in the current slot b/c its bottm neighbor's height, current slot's top neighbor's height might need to be updated again.
        we keep checking until there is no water to be spilled.
"""

"""
Solution 2:
start from boundries, go to inside;
h[new] - h is the water to trap
traversal order: from priority queue

For every point on the border set the water level to the point height
For every point not on the border set the water level to infinity
Put every point on the border into the set of active points
While the set of active points is not empty:
    Select the active point P with minimum level
    Remove P from the set of active points
    For every point Q adjacent to P:
        Level(Q) = max(Height(Q), min(Level(Q), Level(P)))
        If Level(Q) was changed:
            Add Q to the set of active points
"""

import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        if m == 0: return 0
        n = len(heightMap[0])
        if n == 0: return 0
        q = []
        visited = []
        for i in range(m):
            tmpv = [False] * n
            visited.append(tmpv)

        for i in range(n):
            heapq.heappush(q, (heightMap[0][i], 0, i))
            heapq.heappush(q, (heightMap[m-1][i], m-1, i))
            visited[0][i] = True
            visited[m-1][i] = True

        for i in range(1, m-1):
            heapq.heappush(q, (heightMap[i][0], i, 0))
            heapq.heappush(q, (heightMap[i][n-1], i, n-1))
            visited[i][0] = True
            visited[i][n-1] = True

        dirs = [[-1,0], [1,0], [0,-1], [0,1]]
        result = 0
        while len(q) > 0:
            h, i, j = heapq.heappop(q)
            # print('h', h, 'i', i, 'j', j,)
            for ii, jj in dirs:
                tmpi = i + ii
                tmpj = j + jj
                if tmpi >= 0 and tmpi < m and tmpj >=0 and tmpj < n and not visited[tmpi][tmpj]:
                    visited[tmpi][tmpj] = True
                    result += max(0, h-heightMap[tmpi][tmpj])
                    heapq.heappush(q, (max(h, heightMap[tmpi][tmpj]), tmpi, tmpj))
            # print('result', result)
        return result


if __name__ == "__main__":
    a = Solution()
    """
    array = [[1,4,3,1,3,2],
    [3,2,1,3,2,4],
    [2,3,3,2,3,1]]
    """
    array = [[3, 10, 8, 12, 2, 7, 9],
        [7, 1, 11, 3, 8, 1, 10],
        [9, 7, 3, 10, 2, 5, 6],
        [7, 11, 1, 4, 6, 11, 9],
        [4, 5, 8, 12, 3, 4, 2],
        [12, 2, 12, 1, 5, 9, 6],
        [6, 5, 8, 12, 4, 11, 10]]

    print(a.trapRainWater(array))
