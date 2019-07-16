class Solution {
public:
    unordered_map<string, pair<int, int>> memo;
    int stoneGameII(vector<int>& piles) {
        dfs(0, 1, piles);
        return memo["0 1"].first;
    }
    
    pair<int, int> dfs(int idx, int M, vector<int>& piles) {
        string key = pair2str(idx, M);
        if (memo.find(key) != memo.end())
            return memo[key];
        int n = piles.size();
        if (n-idx <= 2 * M) {
            int res = 0;
            for (int i = idx; i < n; ++i)
                res += piles[i];
            memo[key] = {res, 0};
            return memo[key];
        }
        pair<int, int> best = {0, 0};
        for (int i = 1; i <= 2*M; ++i) {
            // idx -> idx + i
            int res = 0;
            for (int j = 0; j < i; ++j)
                res += piles[idx+j];
            auto tmpres = dfs(idx+i, max(M,i), piles);
            pair<int, int> final_res = {res+tmpres.second, tmpres.first};
            if (final_res.first > best.first)
                best = final_res;
        }
        memo[key] = best;
        return memo[key];
    }
    
    string pair2str(int i, int j) {
        return to_string(i) + ' ' + to_string(j);
    }
};
