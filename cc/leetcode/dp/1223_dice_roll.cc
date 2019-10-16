class Solution {
public:
    int dieSimulator(int n, vector<int>& rollMax) {
        vector<vector<int>> memo;
        int MOD = pow(10, 9) + 7;
        for (int i = 0; i < 6; ++i) {
            vector<int> tmp(rollMax[i], 0);
            memo.push_back(tmp);
            memo[i][0] = 1;
        }
        
        for (int k = 0; k < n-1; ++k) {
            vector<vector<int>> new_memo;
            
            vector<int> memo_sum(6, 0);
            int total = 0;
            for (int i = 0; i < 6; ++i) {
                for (int j = 0; j < rollMax[i]; ++j)
                    memo_sum[i] = (memo_sum[i] + memo[i][j]) % MOD;
                total = (total + memo_sum[i]) % MOD;
            }
            
            for (int i = 0; i < 6; ++i) {
                int c = rollMax[i];
                vector<int> tmp(c, 0);
                new_memo.push_back(tmp);
                for (int j = 0; j < c-1; ++j)
                    new_memo[i][j+1] = memo[i][j];
                new_memo[i][0] = (total - memo_sum[i]) % MOD;
            }
            memo = new_memo;
        }
        
        int result = 0;
        for (int i = 0; i < 6; ++i) {
            for (int j = 0; j < memo[i].size(); ++j)
                result = (result + memo[i][j]) % MOD;
        }
        if (result >= 0)
            return result;
        else
            return MOD + result;
    }
};
