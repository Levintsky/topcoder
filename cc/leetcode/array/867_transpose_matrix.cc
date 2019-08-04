class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        vector<vector<int>> res; // n x m
        int m = A.size();
        int n = A[0].size();
        
        for (int i = 0; i < n; ++i) {
            vector<int> tmp(m, 0);
            for (int j = 0; j < m; ++j)
                tmp[j] = A[j][i];
            res.push_back(tmp);
        }
        return res;
    }
};
