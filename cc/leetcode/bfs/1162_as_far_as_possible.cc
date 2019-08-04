class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0)
            return -1;
        int n = grid[0].size();
        if (n == 0)
            return -1;
        queue<pair<int, int>> q1, q2;
        int i, j;
        for (i = 0; i < m; ++i) {
            for (j = 0; j < n; ++j) {
                if (grid[i][j] == 1)
                    q1.push({i, j});
            }
        }
        if (q1.size() == 0 || q1.size() == m * n)
            return -1;
        
        // bfs
        vector<int> di = {0, 0, 1, -1};
        vector<int> dj = {1, -1, 0, 0};
        int curr = 2, res = 0;
        while (q1.size() > 0) {
            while (q1.size() > 0) {
                auto ij = q1.front();
                q1.pop();
                for (i = 0; i < 4; ++i) {
                    int newi = ij.first + di[i];
                    int newj = ij.second + dj[i];
                    if (newi >= 0 && newi < m && newj >= 0 && newj < n && grid[newi][newj] == 0) {
                        grid[newi][newj] = curr;
                        q2.push({newi, newj});
                        res = curr;
                    }
                }
            }
            swap(q1, q2);
            curr++;
        }
        return res - 1;
    }
};
