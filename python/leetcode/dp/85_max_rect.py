"""
85. Maximal Rectangle (Hard)

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        left = [0] * n
        right = [n] * n
        height = [0] * n

        maxA = 0

        for i in range(m):
            curr_left, curr_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(curr_left, left[j])
                else:
                    curr_left = j + 1
                    left[j] = 0  # key!!! for boundary case
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(curr_right, right[j])
                else:
                    right[j] = n
                    curr_right = j
            # update area
            for j in range(n):
                maxA = max(maxA, (right[j] - left[j]) * height[j])
        return maxA


if __name__ == "__main__":
    a = Solution()
    print(
        a.maximalRectangle(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
    )
