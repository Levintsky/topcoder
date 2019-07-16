class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        int i = 0, cnt = 0, res = 0;
        for (int j = 0; j < A.size(); ++j) {
            if (A[j] >= L && A[j] <= R) {
                cnt = j - i + 1;
                res += cnt;
            } else if (A[j] < L)
                res += cnt;
            else {
                i = j + 1;
                cnt = 0;
            }
        }
        return res;
    }
};
