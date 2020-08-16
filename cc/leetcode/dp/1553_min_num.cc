class Solution {
public:
    unordered_map<int, int> memo;
    
    int minDays(int n) {
        if (memo.find(n) != memo.end()) {
            return memo[n];
        } else if (n <= 1) {
            memo[n] = n;
            return memo[n];
        } else {
            int res = 1 + std::min(n % 2 + minDays(n/2), n % 3 + minDays(n/3));
            memo[n] = res;
            return memo[n];
        }
    }
};
