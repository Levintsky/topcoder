class Solution {
public:
    bool valid(const string& a, const string& b) {
        int n = a.size();
        int cnt = 0;
        for (int i=0; i < n; ++i) {
            if (a[i] != b[i])
                cnt++;
            if (cnt >= 3)
                return false;
        }
        return true;
    }
    int numSimilarGroups(vector<string>& A) {
        int n = A.size();
        vector<int> memo(n, -1);
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                if (valid(A[i], A[j])) {
                    int par_i = find_par(memo, i);
                    int par_j = find_par(memo, j);
                    // cout << par_i << " " << par_j << endl;
                    if (par_i > par_j) {
                        memo[par_i] = par_j;
                    } else if (par_i < par_j) {
                        memo[par_j] = par_i;
                    }
                    /*for (int k = 0; k < 4; ++k)
                        cout << memo[k] << " ";
                    cout << endl;*/
                }
            }
        }
        int result = 0;
        for (int i = 0; i < n; ++i) {
            if (memo[i] == -1)
                result++;
        }
        return result;
    }
    
    int find_par(vector<int>& memo, int idx) {
        while (memo[idx] != -1)
            idx = memo[idx];
        return idx;
    }
};
