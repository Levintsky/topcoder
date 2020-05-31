"""
877. Stone Game (Medium)

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 

Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        cum = [0]
        for item in piles:
            cum.append(cum[-1] + item)
        cum = cum[1:]
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if i == j:
                memo[i, j] = piles[i]
                return memo[i, j]
            # option 1: take i
            if i == 0:
                tmp_sum = cum[j]
            else:
                tmp_sum = cum[j] - cum[i-1]
            res1 = tmp_sum - dp(i+1, j)
            res2 = tmp_sum - dp(i, j-1)
            memo[i, j] = max(res1, res2)
            return memo[i, j]
        
        result = dp(0, len(piles)-1)
        # print(memo)
        return result * 2 > sum(piles)


"""
Approach 1: Just return true
Alex is first to pick pile.
piles.length is even, and this lead to an interesting fact:
Alex can always pick odd piles or always pick even piles!

For example,
If Alex wants to pick even indexed piles piles[0], piles[2], ....., piles[n-2],
he picks first piles[0], then Lee can pick either piles[1] or piles[n - 1].
Every turn, Alex can always pick even indexed piles and Lee can only pick odd indexed piles.

In the description, we know that sum(piles) is odd.
If sum(piles[even]) > sum(piles[odd]), Alex just picks all evens and wins.
If sum(piles[even]) < sum(piles[odd]), Alex just picks all odds and wins.

So, Alex always defeats Lee in this game.

C++/Java

    return true;
Python:

    return True

Approach 2: 2D DP
It's tricky when we have even number of piles of stones. You may not have this condition in an interview.

Follow-up:

What if piles.length can be odd?
What if we want to know exactly the diffenerce of score?
Then we need to solve it with DP.

dp[i][j] means the biggest number of stones you can get more than opponent picking piles in piles[i] ~ piles[j].
You can first pick piles[i] or piles[j].

If you pick piles[i], your result will be piles[i] - dp[i + 1][j]
If you pick piles[j], your result will be piles[j] - dp[i][j - 1]
So we get:
dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
We start from smaller subarray and then we use that to calculate bigger subarray.

Note that take evens or take odds, it's just an easy strategy to win when the number of stones is even.
It's not the best solution!
I didn't find a tricky solution when the number of stones is odd (maybe there is).

C++:

    bool stoneGame(vector<int>& p) {
        int n = p.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) dp[i][i] = p[i];
        for (int d = 1; d < n; d++)
            for (int i = 0; i < n - d; i++)
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1]);
        return dp[0][n - 1] > 0;
    }
Java:

    public boolean stoneGame(int[] p) {
        int n = p.length;
        int[][] dp  = new int[n][n];
        for (int i = 0; i < n; i++) dp[i][i] = p[i];
        for (int d = 1; d < n; d++)
            for (int i = 0; i < n - d; i++)
                dp[i][i + d] = Math.max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1]);
        return dp[0][n - 1] > 0;
    }
Python:

    def stoneGame(self, p):
        n = len(p)
        dp = [[0] * n for i in range(n)]
        for i in range(n): dp[i][i] = p[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(p[i] - dp[i + 1][i + d], p[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0

Approach 3: 1D DP
Follow up: Use only O(N) space?

Simplify to 1D DP.

C++:

    bool stoneGame(vector<int>& p) {
        vector<int> dp = p;
        for (int d = 1; d < p.size(); d++)
            for (int i = 0; i < p.size() - d; i++)
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i]);
        return dp[0] > 0;
    }
Java:

    public boolean stoneGame(int[] p) {
        int[] dp = Arrays.copyOf(p, p.length);;
        for (int d = 1; d < p.length; d++)
            for (int i = 0; i < p.length - d; i++)
                dp[i] = Math.max(p[i] - dp[i + 1], p[i + d] - dp[i]);
        return dp[0] > 0;
    }
Python:

    def stoneGame(self, p):
        n = len(p)
        dp = p[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
        return dp[0] > 0
"""