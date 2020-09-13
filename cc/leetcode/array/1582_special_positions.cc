class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        
        vector<int> arr_r(m, 0);
        vector<int> arr_c(n, 0);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                arr_r[i] += mat[i][j];
                arr_c[j] += mat[i][j];
            }
        }
        
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (arr_r[i] == 1 && arr_c[j] == 1 && mat[i][j] == 1)
                    res++;
            }
        }
        return res;
    }
};
