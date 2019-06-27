"""
1033. Moving Stones Until Consecutive (Easy)

Three stones are on a number line at positions a, b, and c.

Each turn, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

Example 1:

Input: a = 1, b = 2, c = 5
Output: [1, 2]
Explanation: Move stone from 5 to 4 then to 3, or we can move it directly to 3.

Example 2:

Input: a = 4, b = 3, c = 2
Output: [0, 0]
Explanation: We cannot make any moves.

Note:

1 <= a <= 100
1 <= b <= 100
1 <= c <= 100
a != b, b != c, c != a
"""


class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x = min(a, b, c)
        z = max(a, b, c)
        y = a + b + c - x - z
        if y - x == 1 and z - y == 1:
            return [0, 0]
        if y - x <= 2 or z - y <= 2:
            min_ = 1
        else:
            min_ = 2
        max_ = (y - x - 1) + (z - y - 1)
        return [min_, max_]


if __name__ == "__main__":
    a = Solution()
    print(a.numMovesStones(1, 2, 5))
    print(a.numMovesStones(4, 3, 2))
