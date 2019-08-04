class Solution {
public:
    int numRollsToTarget(int d, int f, int target) {
        array<long, 1001> memo1;
        array<long, 1001> memo2;
        long MOD = pow(10, 9) + 7;
        fill(memo1.begin(), memo1.end(), 0);
        for (int i = 1; i <= f; ++i)
            memo1[i] = 1;
        for (int dd=0; dd<d-1; ++dd) {
            fill(memo2.begin(), memo2.end(), 0);
            for (int i = 1; i <= target; ++i) {
                for (int j = max(i-f, 1); j<i; ++j) {
                    memo2[i] = (memo2[i] + memo1[j]) % MOD;
                }
            }
            swap(memo2, memo1);
        }
        return memo1[target];
    }
};
