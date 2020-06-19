"""
887. Super Egg Drop (Hard)

You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4
 

Note:

1 <= K <= 100
1 <= N <= 10000
"""

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # f(K, M) = f(K, M-1) + f(K-1, M-1) + 1
        l, r = 1, N
        memo = {}
        
        def get(K, m):
            if (K, m) in memo:
                return memo[K, m]
            if K == 1:
                memo[K, m] = m
            elif m == 1:
                memo[K, m] = 1
            else:
                memo[K, m] = 1 + get(K-1, m-1) + get(K, m-1)
            return memo[K, m]
        
        best = N
        while l <= r:
            mid = (l + r) // 2
            
            # get memo[K, mid]
            # print(mid)
            if get(K, mid) >= N:
                best = min(best, mid)
                r = mid - 1
            else:
                l = mid + 1
        # print(memo)
        return best

    def solve2(self, K, N):
        memo = []
        for i in range(K+1):
            memo.append([0] * (N+1))
        for j in range(1, N+1):
            for i in range(1, K+1):
                memo[i][j] = memo[i-1][j-1] + memo[i][j-1] + 1
                if memo[i][j] >= N:
                    return j


if __name__ == "__main__":
    a = Solution()
    """
    print(a.superEggDrop(1, 2))
    print(a.superEggDrop(2, 6))
    print(a.superEggDrop(3, 14))
    """

    print(a.solve2(1, 2))
    print(a.solve2(2, 6))
    print(a.solve2(3, 14))
