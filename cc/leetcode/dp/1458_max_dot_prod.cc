class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        vector<vector<int>> v(n1, vector<int>(n2));
        for (int i = 0; i < n1; ++i) {
            for (int j = 0; j < n2; ++j) {
                v[i][j] = nums1[i] * nums2[j];
                if (i > 0 && j > 0)
                    v[i][j] = max(v[i][j], v[i-1][j-1] + nums1[i] * nums2[j]);
                if (i > 0)
                    v[i][j] = max(v[i][j], v[i-1][j]);
                if (j > 0)
                    v[i][j] = max(v[i][j], v[i][j-1]);
            }
        }
        return v[n1-1][n2-1];
    }
};
