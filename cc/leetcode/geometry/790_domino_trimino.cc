class Solution {
public:
    int numTilings(int N) {
        vector<long> res = {1,1,2,5}; // 0,1,2,3
        if (N < 3)
            return res[N];
        long accum = 2;
        long MOD = pow(10, 9) + 7;
        for (int i = 4; i < N+1; ++i) {
            long tmp = (res[i-1] + res[i-2] + accum * 2) % MOD;
            accum = (accum + res[i-2]) % MOD;
            res.push_back(tmp);
        }
        return res.back();
    }
};
