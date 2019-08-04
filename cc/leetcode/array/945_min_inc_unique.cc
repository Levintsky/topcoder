class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {
        sort(A.begin(), A.end());
        A.push_back(INT_MAX);
        vector<int> tmp;
        int result = 0;
        for (int i = 1; i < A.size(); ++i) {
            if (A[i] == A[i-1])
                tmp.push_back(A[i]);
            if (A[i] - A[i-1] > 1) {
                for (int j = A[i-1]+1; j < A[i]; ++j) {
                    if (tmp.size() > 0) {
                        result += j - tmp.back();
                        tmp.pop_back();
                    } else
                        break;
                }
            }
        }
        return result;
    }
};

// Smarter!
int minIncrementForUnique(vector<int>& A) {
        sort(A.begin(), A.end());
        int res = 0, need = 0;
        for (int a: A) {
            res += max(need - a, 0);
            need = max(a, need)+1;
        }
        return res;
    }
