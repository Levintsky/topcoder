class Solution {
public:
    int uniqueLetterString(string s) {
        vector<vector<int>> memo(26, vector<int>(0));
        int ns = s.size();
        for (int i = 0; i < ns; ++i) {
            int idx = s[i] - 'A';
            memo[idx].push_back(i);
        }
        long res = 0;
        long MOD = pow(10, 9) + 7;
        int left, right;
        
        for (int i=0; i < 26; ++i) {
            int n = memo[i].size();
            if (n == 0)
                continue;
            for (int j = 0; j < n; ++j) {
                if (j == 0)
                    left = 0;
                else
                    left = memo[i][j-1]+1;
                if (j == n-1)
                    right = ns -1;
                else
                    right = memo[i][j+1]-1;
                res = (res + (memo[i][j]-left+1) * (right-memo[i][j]+1)) % MOD;
            }
        }
        return res;
    }
};
