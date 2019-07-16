class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0)
            return 0;
        int n = grid[0].size();
    int res = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (grid[i][j] == 0)
                continue;
            // up
            if (i == 0)
                res++;
            else if (i > 0 && grid[i-1][j] == 0)
                res++;
            // down
            if (i == m-1)
                res++;
            else if (i < m-1 && grid[i+1][j] == 0)
                res++;
            // left
            if (j == 0)
                res++;
            else if (j > 0 && grid[i][j-1] == 0)
                res++;
            // right
            if (j == n-1)
                res++;
            else if (j < n-1 && grid[i][j+1] == 0)
                res++;
        }
    }
    return res;
    }

};
