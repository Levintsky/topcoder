class Solution {
public:
    int numPermsDISequence(string S) {
        int n = S.size() + 1;
        unordered_map<int, int> memo, memo1;
        memo[0] = 1;
        long MOD = pow(10, 9) + 7;
        int curr = 1;
        for (char c : S) {
            memo1.clear();
            for (auto item : memo) {
                int k = item.first, v = item.second;
                for (int replace = 0; replace < curr; ++replace) {
                    if (replace != k) {
                        if ((k > replace && c == 'D') || (k < replace && c == 'I'))
                            memo1[replace] = (memo1[replace] + memo[k]) % MOD;
                    } else {
                        if (c == 'D')
                            memo1[replace] = (memo1[replace] + memo[k]) % MOD;
                    }
                }
            }
            if (c == 'I') {
                for (auto item : memo)
                    memo1[curr] = (memo1[curr] + item.second) % MOD;
            }
            swap(memo, memo1);
            curr++;
        }
        int result = 0;
        for (auto item : memo)
            result = (result + item.second) % MOD;
        return result;
    }
};

// Better solution
class Solution {
public:
    int numPermsDISequence(string S) {
        int n = S.size() + 1;
        vector<int> dp(n, 1);
        long MOD = pow(10, 9) + 7;
        for (char c : S) {
            n--;
            vector<int> dp2(dp.size()-1, 0);
            if (c == 'D') {
                for (int i = n-1; i >= 0; --i) {
                    if (i == n-1)
                        dp2[i] = dp[i+1];
                    else
                        dp2[i] = (dp2[i+1] + dp[i+1]) % MOD;
                }
            } else {
                for (int i = 0; i < n; ++i) {
                    if (i == 0)
                        dp2[i] = dp[i];
                    else
                        dp2[i] = (dp2[i-1] + dp[i]) % MOD;
                }
            }
            swap(dp, dp2);
        }
        return dp[0];
    }
};
