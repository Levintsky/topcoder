class Solution {
public:
    int arrangeCoins(int n) {
        if (n == 0)
            return 0;
        long item = n;
        item *= 2;
        long res = sqrt(item);
        if (res * (res+1) / 2 > n)
            return res - 1;
        else
            return res;
    }
};
