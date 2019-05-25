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


class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        n = len(stones)
        if K > 2 and n % (K-1) != 1:
            return -1

        cnt = 0
        while len(stones) > 1:
            stones_new = [sum(stones[:K])]
            n = len(stones)
            for i in range(n - K):
                tmp = stones_new[-1] - stones[i] + stones[K+i]
                stones_new.append(tmp)
            # find minimum
            min_sum, min_id = stones_new[0], 0
            for idx, sum_ in enumerate(stones_new):
                if sum_ < min_sum:
                    min_id, min_sum = idx, sum_
            # merge the minimum
            stones_ = stones[:min_id]
            stones_.append(min_sum)
            stones_ += stones[min_id+K:]
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
            prefix[i+1] = prefix[i] + stones[i]

        for m in range(K, n+1): # distance
            for i in range(n-m+1):
                j = i + m - 1
                dp[i][j] = min([dp[i][mid] + dp[mid + 1][j] for mid in range(i, j, K-1)])
                if (j - i) % (K - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]
        return dp[0][n - 1]

if __name__ == "__main__":
    a = Solution()
    print(a.mergeStones([3,2,4,1], 2))
    print(a.mergeStones([3,2,4,1], 3))
    print(a.mergeStones([3,5,1,2,6], 3))
