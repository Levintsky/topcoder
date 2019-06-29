"""
1000. Minimum Cost to Merge Stones (Hard)

There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.

Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""

"""
Solution 1: 3D DP
Intuition
Seem that most of games, especially stone games, are solved by dp?

Explanation

dp[i][j][m] means the cost needed to merge stone[i] ~ stones[j] into m piles.

Initial status dp[i][i][1] = 0 and dp[i][i][m] = infinity

dp[i][j][1] = dp[i][j][k] + stonesNumber[i][j]
dp[i][j][m] = min(dp[i][mid][1] + dp[mid + 1][j][m - 1])

The origine python2 solution is a bit too long on the memorization part.
So I rewrote it in python3 with cache helper,
so it will be clear for logic.

Complexity
Time O(N^3/K), Space O(KN^2)

Python3:

    def mergeStones(self, stones, K):
        n = len(stones)
        inf = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]
            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))
        res = dp(0, n - 1, 1)
        return res if res < inf else -1

Solution 2: 2D DP
Explanation
Suggested by @yaoct, we can simplify the third parameter m in DP.

stones[i] ~ stones[j] will merge as much as possible.

Finally (j - i) % (K - 1) + 1 piles will be left.

It's less than K piles and no more merger happens.

dp[i][j] means the minimum cost needed to merge stones[i] ~ stones[j].

Complexity
Time O(N^3/K) Space O(N^2)
It can be improved, but I think it's fine now.

Java

    public int mergeStones(int[] stones, int K) {
        int n = stones.length;
        if ((n - 1) % (K - 1) > 0) return -1;

        int[] prefix = new int[n+1];
        for (int i = 0; i <  n; i++)
            prefix[i + 1] = prefix[i] + stones[i];

        int[][] dp = new int[n][n];
        for (int m = K; m <= n; ++m)
            for (int i = 0; i + m <= n; ++i) {
                int j = i + m - 1;
                dp[i][j] = Integer.MAX_VALUE;
                for (int mid = i; mid < j; mid += K - 1)
                    dp[i][j] = Math.min(dp[i][j], dp[i][mid] + dp[mid + 1][j]);
                if ((j - i) % (K - 1) == 0)
                    dp[i][j] += prefix[j + 1] - prefix[i];
            }
        return dp[0][n - 1];
    }
C++

    int mergeStones(vector<int>& stones, int K) {
        int n = stones.size();
        if ((n - 1) % (K - 1)) return -1;

        vector<int> prefix(n + 1);
        for (int i = 0; i <  n; i++)
            prefix[i + 1] = prefix[i] + stones[i];

        vector<vector<int> > dp(n, vector<int>(n));
        for (int m = K; m <= n; ++m)
            for (int i = 0; i + m <= n; ++i) {
                int j = i + m - 1;
                dp[i][j] = INT_MAX;
                for (int mid = i; mid < j; mid += K - 1)
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j]);
                if ((j - i) % (K - 1) == 0)
                    dp[i][j] += prefix[j + 1] - prefix[i];
            }
        return dp[0][n - 1];
    }
Python3

    def mergeStones(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res
        return dp(0, n - 1)

FAQ
Q: Why mid jump at step K - 1
A: We can merge K piles into one pile,
we can't merge K + 1 piles into one pile.
We can merge K + K - 1 piles into on pile,
We can merge K + (K - 1) * steps piles into one pile.


Update 2019-03-04
Sorry guys, It seems that somehow it started kind of debate in one of my replies.
I didn't mean to do that and I feel I have to say something.

Yes, I agree that people have right to express in their comfortable language, including Chinese.
It's not the same as the situation of a meeting room.
User don't take others' time and force them to listen to you.
Reader can choose what they want to read.
Like ebooker and trip adviser, they have comments in all languages.

I strongly disagree any unreasonable downvotes.
Posts and reply should not be downvoted for no reason like language.
Personally I receive downvotes for each of my posts.
Of course, people have right to do that but please at least say something or leave a message.
Like "I downvote for the reason that....", so that I can also improve somehow, right?

I encourage everyone to express in English and discuss with all others.
The main reason is that English is still one important skill for engineers.
We need to learn from documents in English.
Moreover, as a Chinese engineer, I hope I can bring the good stuff back to the world.

In the end, the most important, I encourage everyone to learn some Chinese :)
"""

class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if K > 2 and n % (K - 1) != 1:
            return -1

        cnt = 0
        while len(stones) > 1:
            stones_new = [sum(stones[:K])]
            n = len(stones)
            for i in range(n - K):
                tmp = stones_new[-1] - stones[i] + stones[K + i]
                stones_new.append(tmp)
            # find minimum
            min_sum, min_id = stones_new[0], 0
            for idx, sum_ in enumerate(stones_new):
                if sum_ < min_sum:
                    min_id, min_sum = idx, sum_
            # merge the minimum
            stones_ = stones[:min_id]
            stones_.append(min_sum)
            stones_ += stones[min_id + K :]
            cnt += min_sum
            stones = stones_
        return cnt

    def solve2(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        dp = []
        for i in range(n):
            dp.append([0] * n)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        for m in range(K, n + 1):  # distance
            for i in range(n - m + 1):
                j = i + m - 1
                dp[i][j] = min(
                    [dp[i][mid] + dp[mid + 1][j] for mid in range(i, j, K - 1)]
                )
                if (j - i) % (K - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]
        return dp[0][n - 1]


if __name__ == "__main__":
    a = Solution()
    print(a.mergeStones([3, 2, 4, 1], 2))
    print(a.mergeStones([3, 2, 4, 1], 3))
    print(a.mergeStones([3, 5, 1, 2, 6], 3))
