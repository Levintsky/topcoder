class Solution {
public:
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        int res = 0, n = x.size(), closest, cur;
        for (int p : {1, -1}) {
            for (int q : {1, -1}) {
                closest = p * x[0] + q * y[0] + 0;
                for (int i = 1; i < n; ++i) {
                    cur = p * x[i] + q * y[i] + i;
                    res = max(res, cur - closest);
                    closest = min(closest, cur);
                }
            }
        }
        return res;
    }
};
