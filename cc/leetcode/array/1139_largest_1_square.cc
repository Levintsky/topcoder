class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> rows, cols;
        for (int i = 0; i < m; ++i) {
            vector<int> tmp1(n, 0), tmp2(n, 0);
            rows.push_back(tmp1);
            cols.push_back(tmp2);
        }
        
        // preprocess
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    if (j == 0)
                        rows[i][j] = 1;
                    else
                        rows[i][j] = rows[i][j-1] + 1;
                    if (i == 0)
                        cols[i][j] = 1;
                    else
                        cols[i][j] = cols[i-1][j] + 1;
                }
            }
        }
        // res
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int side = min(i+1, j+1);
                while (side >= res + 1) {
                    if (rows[i][j]>=side && cols[i][j]>=side && rows[i-side+1][j]>=side && cols[i][j-side+1]>=side) {
                        res = side;
                        break;
                    }
                    side--;
                }
            }
        }
        return res * res;
    }
};
