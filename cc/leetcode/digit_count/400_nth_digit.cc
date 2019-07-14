class Solution {
public:
    int findNthDigit(int n) {
        long begin = 1, end = 9;
        int c = 1;
        while (true) {
            long all = (end - begin + 1) * c;
            if (all < n) {
                n -= all;
                begin = begin * 10;
                end = (end + 1) * 10 - 1;
                c++;
            } else {
                long num = (n-1) / c + begin;
                int digit = (n-1) % c + 1;
                int base = int(pow(10, c-digit));
                int res = (num / base) % 10;
                return res;
            }
        }
        return -1;
    }
};
