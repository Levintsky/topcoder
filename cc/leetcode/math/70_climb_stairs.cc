class Solution {
public:
    int climbStairs(int n) {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;
        int last = 1, next = 2;
        for (int i = 3; i <= n; ++i) {
            next = last + next;
            last = next - last;
        }
        return next;
    }
};