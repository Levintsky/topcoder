"""
1197. Minimum Knight Moves (Medium)

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.



Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300
"""

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if (x, y) == (0, 0):
            return 0
        
        # closer enough
        x, y = abs(x), abs(y)
        res = 0
        while x > 8 or y > 8:
            if abs(y) > abs(x):
                if y > 0:
                    y -= 2
                else:
                    y += 2
                if x > 0:
                    x -= 1
                else:
                    x += 1
            else:
                if y > 0:
                    y -= 1
                else:
                    y += 1
                if x > 0:
                    x -= 2
                else:
                    x += 2                
            res += 1
        
        # bfs
        q = deque()
        q.append((0, 0))
        visited = set()
        while len(q) > 0:
            q2 = set()
            while len(q) > 0:
                i, j = q.pop()
                if (i, j) == (x, y):
                    return res
                visited.add((i, j))
                for di, dj in [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]:
                    ii, jj = i+di, j+dj
                    if (ii, jj) not in visited:
                        q2.add((ii, jj))
            for item in q2:
                q.append(item)
            res += 1
        return
    
    def solve2(self, x: int, y: int) -> int:
        @lru_cache(None) 
        def DP(x,y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(DP(abs(x-1),abs(y-2)),DP(abs(x-2),abs(y-1)))+1
        return DP(abs(x),abs(y))
                    