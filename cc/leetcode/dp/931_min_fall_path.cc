class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& A) {
        int n = A.size();
        if (n == 0)
            return 0;
        int m = A[0].size();
        vector<int> result(A[0].begin(), A[0].end());
        vector<int> result2(m, 0);
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                result2[j] = result[j];
                if (j > 0)
                    result2[j] = min(result[j-1], result2[j]);
                if (j != m - 1)
                    result2[j] = min(result[j+1], result2[j]);
                result2[j] += A[i][j];
            }
            swap(result, result2);
        }
        int final_result = INT_MAX;
        for (int item : result)
            final_result = min(final_result, item);
        return final_result;
    }
};
