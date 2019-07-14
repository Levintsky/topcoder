class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            int x = a ^ b;
            int y = (a & b) & INT_MAX;
            y = y << 1;
            a = x;
            b = y;
        }
        return a;
    }
};