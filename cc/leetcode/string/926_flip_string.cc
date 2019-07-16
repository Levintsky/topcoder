class Solution {
public:
    int minFlipsMonoIncr(string S) {
        int n = S.size();
        int res = 0;
        int i;
        for (i = 0; i < n; ++i) {
            if (S[i] == '1')
                ++res;
        }
        int tmp = res;
        for (i = n-1; i >= 0; --i) {
            if (S[i] == '0')
                ++tmp;
            else
                --tmp;
            res = min(res, tmp);
        }
        return res;
    }
};
