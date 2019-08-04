class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.size(), n = text2.size();
        vector<vector<int>> arr;
        for (int i = 0; i < m+1; ++i)
            arr.push_back(vector<int>(n+1, 0));
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (text1[i] == text2[j])
                    arr[i+1][j+1] = arr[i][j] + 1;
                else
                    arr[i+1][j+1] = max(arr[i+1][j], arr[i][j+1]);
            }
        }
        return arr[m][n];
    }
};
