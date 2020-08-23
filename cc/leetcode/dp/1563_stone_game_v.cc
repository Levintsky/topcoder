class Solution {
public:
    unordered_map<int, int> memo;
    
    int dp(int i, int j, vector<int>& prefix, vector<int>& s) {
        int key = i * 501 + j;
        if (memo.find(key) != memo.end())
            return memo[key];
        if (i >= j)
            return 0;
        if (i + 1 == j) {
            memo[key] = min(s[i], s[j]);
            return memo[key];
        }
        int best = 0;
        for (int k = i; k < j; ++k) {
            int sum_l = prefix[k+1] - prefix[i];
            int sum_r = prefix[j+1] - prefix[k+1];
            if (sum_l >= sum_r)
                best = max(best, sum_r + dp(k+1, j, prefix, s));
            if (sum_r >= sum_l)
                best = max(best, sum_l + dp(i, k, prefix, s));
        }
        memo[key] = best;
        return best;
    }
    
    int stoneGameV(vector<int>& stoneValue) {
        vector<int> prefix(1, 0);
        for (int item : stoneValue) 
            prefix.push_back(prefix.back() + item);
        
        return dp(0, stoneValue.size()-1, prefix, stoneValue);
    }
};
