class Solution {
public:
    int findComplement(int num) {
        int res = 0;
        long base = 1;
        while (num > 0) {
            if ((num & 1) == 0)
                res += base;
            base *= 2;
            num /= 2;
        }
        return res;
    }
};
