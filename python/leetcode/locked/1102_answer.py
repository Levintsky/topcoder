"""
Since heappop() only pop the smallest number from the queue, but what I want is the element with the highest score so far, so I change all scores to negative number, so that I can pop the element with highest score.

Notice: memo is used to store the cells that have been visited.
"""

class Solution:
    def maximumMinimumPath(self, matrix: List[List[int]]) -> int:
        de = ((1,0),(0,1),(-1,0),(0,-1))
        rl, cl = len(matrix), len(matrix[0])
        q = [(-matrix[0][0],0,0)]
        memo = [[1 for _ in range(cl)] for _ in range(rl)]
        while q:
            t, x, y = heapq.heappop(q)
            if x == rl - 1 and y == cl - 1:
                return -t
            for d in de:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < rl and 0 <= ny < cl and memo[nx][ny]:
                    memo[nx][ny] = 0
                    heapq.heappush(q, (max(t, -matrix[nx][ny]), nx, ny))