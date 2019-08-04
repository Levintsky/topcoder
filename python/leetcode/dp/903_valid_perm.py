"""
903. Valid Permutations for DI Sequence (Hard)

We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

Example 1:

Input: "DID"
Output: 5
Explanation: 
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.
"""

class Solution(object):
    # logically correct
    # too slow! O(n^3)
    # cpp version could pass
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S) + 1
        memo = {0: 1} # end with 0, 1
        new_memo = {}
        curr = 1
        MOD = 10 ** 9 + 7
        for c in S:
            for k, v in memo.items():
                # exchange xxxxreplacexxx | curr
                for replace in range(curr):
                    # xxxxx | replace
                    # case 1: replace != k
                    if replace != k:
                        if (k > replace and c == 'D') or (k < replace and c == 'I'):
                            new_memo[replace] = (new_memo.get(replace, 0) + memo[k]) % MOD
                    else:
                        # case 2: replace == k
                        # xxxxcurr | replace
                        if c == 'D':
                            new_memo[replace] = (new_memo.get(replace, 0) + memo[k]) % MOD
            if c == 'I':
                new_memo[curr] = sum(memo.values()) % MOD
            memo, new_memo = new_memo, {}
            # print(memo)
            curr += 1
        return sum(memo.values()) % MOD

    def solve2(self, S):
        n = len(S) + 1
        dp = [1] * n
        MOD = 10 ** 9 + 7
        for c in S:
            n -= 1
            dp2 = [0] * n
            if c == 'D':
                for i in range(n-1, -1, -1):
                    if i == n-1:
                        dp2[i] = dp[i+1]
                    else:
                        dp2[i] = (dp2[i+1] + dp[i+1]) % MOD
            else:
                for i in range(n):
                    if i == 0:
                        dp2[i] = dp[i]
                    else:
                        dp2[i] = (dp2[i-1] + dp[i]) % MOD
            dp = [item for item in dp2]
        return dp[0]

if __name__ == "__main__":
    a = Solution()
    # print(a.numPermsDISequence("DID"))
    print(a.solve2("DID"))

"""
Intuition:

This the only problem this week that I feel like writing a solution.
But don't know how to explain.

dp[i][j] means the number of possible permutations of first i + 1 digits,
where the i + 1th digit is j + 1th smallest in the rest of digits.

Ok, may not make sense ... Let's see the following diagram

I take the example of S = "DID".
The permutation can start from 1, 2, 3, 4.
So dp[0][0] = dp[0][1] = dp[0][2] = dp[0][3] = 1.
In the parenthesis, I list all possible permutations.

We decrese from the first digit to the second,
the down arrow show the all possibile decresing pathes.

The same, cause we increase from the second digit to the third,
the up arrow show the all possibile increasing pathes.

dp[2][1] = 5, mean the number of permutations
where the third digitis the second smallest of the rest.
We have 413,314,214,423,324.
Fow example 413, where 2,3 are left and 3 the second smallest of them.

Explanation:
As shown in the diagram,
for "I", we calculate prefix sum of the array,
for "D", we calculate sufixsum of the array.

Time Complexity:
O(N^2)

C++:

    int numPermsDISequence(string S) {
        int n = S.length(), mod = 1e9 + 7;
        vector<vector<int>> dp(n + 1, vector<int>(n + 1));
        for (int j = 0; j <= n; j++) dp[0][j] = 1;
        for (int i = 0; i < n; i++)
            if (S[i] == 'I')
                for (int j = 0, cur = 0; j < n - i; j++)
                    dp[i + 1][j] = cur = (cur + dp[i][j]) % mod;
            else
                for (int j = n - i - 1, cur = 0; j >= 0; j--)
                    dp[i + 1][j] = cur = (cur + dp[i][j + 1]) % mod;
        return dp[n][0];
    }
Java:

    public int numPermsDISequence(String S) {
        int n = S.length(), mod = (int)1e9 + 7;
        int[][] dp = new int[n + 1][n + 1];
        for (int j = 0; j <= n; j++) dp[0][j] = 1;
        for (int i = 0; i < n; i++)
            if (S.charAt(i) == 'I')
                for (int j = 0, cur = 0; j < n - i; j++)
                    dp[i + 1][j] = cur = (cur + dp[i][j]) % mod;
            else
                for (int j = n - i - 1, cur = 0; j >= 0; j--)
                    dp[i + 1][j] = cur = (cur + dp[i][j + 1]) % mod;
        return dp[n][0];
    }
Now as we did for every DP, make it 1D dp.
Reminded by @apple702, in the Java solution, it should be dp=Arrays.copyOf(dp2, n);
Otherwise it passes an address.

C++:

    int numPermsDISequence(string S) {
        int n = S.length(), mod = 1e9 + 7;
        vector<int> dp(n + 1, 1), dp2(n);
        for (int i = 0; i < n; dp = dp2, i++) {
            if (S[i] == 'I')
                for (int j = 0, cur = 0; j < n - i; j++)
                    dp2[j] = cur = (cur + dp[j]) % mod;
            else
                for (int j = n - i - 1, cur = 0; j >= 0; j--)
                    dp2[j] = cur = (cur + dp[j + 1]) % mod;
        }
        return dp[0];
    }
Java:

    public int numPermsDISequence(String S) {
        int n = S.length(), mod = (int)1e9 + 7;
        int[] dp = new int[n + 1], dp2 = new int[n];;
        for (int j = 0; j <= n; j++) dp[j] = 1;
        for (int i = 0; i < n; i++) {
            if (S.charAt(i) == 'I')
                for (int j = 0, cur = 0; j < n - i; j++)
                    dp2[j] = cur = (cur + dp[j]) % mod;
            else
                for (int j = n - i - 1, cur = 0; j >= 0; j--)
                    dp2[j] = cur = (cur + dp[j + 1]) % mod;
            dp = Arrays.copyOf(dp2, n);
        }
        return dp[0];
    }
Python:

    def numPermsDISequence(self, S):
        dp = [1] * (len(S) + 1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)
"""