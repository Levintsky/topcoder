"""
1040. Moving Stones Until Consecutive II (Medium)

On an infinite number line, the position of the i-th stone is given by stones[i].  Call a stone an endpoint stone if it has the smallest or largest position.

Each turn, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.

In particular, if the stones are at say, stones = [1,2,5], you cannot move the endpoint stone at position 5, since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

Example 1:

Input: [7,4,9]
Output: [1,2]
Explanation: 
We can move 4 -> 8 for one move to finish the game.
Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
Example 2:

Input: [6,5,4,3,10]
Output: [2,3]
We can move 3 -> 8 then 10 -> 7 to finish the game.
Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.
Example 3:

Input: [100,101,104,102,103]
Output: [0,0]

Note:

3 <= stones.length <= 10^4
1 <= stones[i] <= 10^9
stones[i] have distinct values.
"""

"""
Lower Bound
As I mentioned in my video last week,
in case of n stones,
we need to find a consecutive n positions and move the stones in.

This idea led the solution with sliding windows.

Slide a window of size N, and find how many stones are already in this window.
We want moves other stones into this window.
For each missing stone, we need at least one move.

Generally, the number of missing stones and the moves we need are the same.
Only one corner case in this problem, we need to move the endpoint to no endpoint.

For case 1,2,4,5,10,
1 move needed from 10 to 3.

For case 1,2,3,4,10,
2 move needed from 1 to 6, then from 10 to 5.


Upper Bound
We try to move all stones to leftmost or rightmost.
For example of to rightmost.
We move the A[0] to A[1] + 1.
Then each time, we pick the stone of left endpoint, move it to the next empty position.
During this process, the position of leftmost stones increment 1 by 1 each time.
Until the leftmost is at A[n - 1] - n + 1.


Complexity
Time of quick sorting O(NlogN)
Time of sliding window O(N)
Space O(1)


Java:

    public int[] numMovesStonesII(int[] A) {
        Arrays.sort(A);
        int i = 0, n = A.length, low = n;
        int high = Math.max(A[n - 1] - n + 2 - A[1], A[n - 2] - A[0] - n + 2);
        for (int j = 0; j < n; ++j) {
            while (A[j] - A[i] >= n) ++i;
            if (j - i + 1 == n - 1 && A[j] - A[i] == n - 2)
                low = Math.min(low, 2);
            else
                low = Math.min(low, n - (j - i + 1));
        }
        return new int[] {low, high};
    }
C++:

    vector<int> numMovesStonesII(vector<int>& A) {
        sort(A.begin(), A.end());
        int i = 0, n = A.size(), low = n;
        int high = max(A[n - 1] - n + 2 - A[1], A[n - 2] - A[0] - n + 2);
        for (int j = 0; j < n; ++j) {
            while (A[j] - A[i] >= n) ++i;
            if (j - i + 1 == n - 1 && A[j] - A[i] == n - 2)
                low = min(low, 2);
            else
                low = min(low, n - (j - i + 1));
        }
        return {low, high};
    }
Python:

    def numMovesStonesII(self, A):
        A.sort()
        i, n, low = 0, len(A), len(A)
        high = max(A[-1] - n + 2 - A[1], A[-2] - A[0] - n + 2)
        for j in range(n):
            while A[j] - A[i] >= n: i += 1
            if j - i + 1 == n - 1 and A[j] - A[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]
"""


class Solution(object):
    def numMovesStonesII(self, A):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        A.sort()
        i, n, low = 0, len(A), len(A)
        # maximum of moving leftmost and moving rightmost
        # e.g. [1, 4, 10, 28]
        #   left case: [4, 5, 10, 28], [5, 6, 10, 28], ...
        #   right case: [1, 4, 9, 10], [1, 4, 8, 9], ...
        # result is maximum of the interval, minus the empty slots in between
        high = max(A[-1] - n + 2 - A[1], A[-2] - A[0] - n + 2)
        for j in range(n):
            # largest sliding window with <n elements A[i]..A[j]
            while A[j] - A[i] >= n:
                i += 1
            # corner case like [1,2,3,4,10] or [0,5,6,7,8]
            if j - i + 1 == n - 1 and A[j] - A[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]


if __name__ == "__main__":
    a = Solution()
    print(a.numMovesStonesII([1, 2, 3, 4, 10, 11]))
