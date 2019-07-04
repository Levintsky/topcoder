"""
1020. Number of Enclaves (Medium)

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.
 

Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""


class Solution:
    # def numEnclaves(self, A: List[List[int]]) -> int:
    def numEnclaves(self, A):
        m = len(A)
        if m == 0:
            return 0
        n = len(A[0])
        if n == 0:
            return 0

        # go through 4 sides
        new_set = []
        visited = set()
        for i in range(n):
            if A[0][i] == 1:
                new_set.append((0, i))
            if A[m - 1][i] == 1:
                new_set.append((m - 1, 1))
        for i in range(1, m - 1):
            if A[i][0] == 1:
                new_set.append((i, 0))
            if A[i][n - 1] == 1:
                new_set.append((i, n - 1))

        # travserse
        while len(new_set) > 0:
            i, j = new_set.pop()
            A[i][j] = 0
            if (i, j) not in visited:
                visited.add((i, j))
                if i > 0 and A[i - 1][j] == 1 and (i - 1, j) not in visited:
                    new_set.append((i - 1, j))
                if i < m - 1 and A[i + 1][j] == 1 and (i + 1, j) not in visited:
                    new_set.append((i + 1, j))
                if j > 0 and A[i][j - 1] == 1 and (i, j - 1) not in visited:
                    new_set.append((i, j - 1))
                if j < n - 1 and A[i][j + 1] == 1 and (i, j + 1) not in visited:
                    new_set.append((i, j + 1))
        result = [sum(item) for item in A]
        return sum(result)


if __name__ == "__main__":
    a = Solution()
    print(a.numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]))
    print(a.numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
    array = [
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    ]
    print(a.numEnclaves(array))
