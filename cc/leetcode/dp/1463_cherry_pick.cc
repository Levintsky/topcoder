class Solution {
public:
    /*int encode(int i, j) {
        return i * 100 + j;
    }*/
    int cherryPickup(vector<vector<int>>& grid) {
        unordered_map<int, int> memo, memo2;
        
        int m = grid.size(), n = grid[0].size();
        memo[n-1] = grid[0][0] + grid[0][n-1];
        
        for (int i = 1; i < m; ++i) {
            memo2.clear();
            
            for (auto kv : memo) {
                int k = kv.first;
                int val = kv.second;
                
                int j1 = k / 100, j2 = k % 100;
                
                for (int jj1 = j1-1; jj1 <= j1+1; jj1++) {
                    for (int jj2 = j2-1; jj2 <= j2+1; jj2++) {
                        if (jj1 < 0 || jj2 < 0 || jj1 >= n || jj2 >= n)
                            continue;
                        int v = grid[i][jj1] + grid[i][jj2] + val;
                        if (jj1 == jj2)
                            v -= grid[i][jj1];
                        memo2[jj1*100+jj2] = max(memo2[jj1*100+jj2], v);
                    }
                }
            }
            swap(memo, memo2);
        }
        
        int res = 0;
        for (auto item : memo)
            res = max(res, item.second);
        return res;
    }
};
