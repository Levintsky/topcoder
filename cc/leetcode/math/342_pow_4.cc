class Solution {
public:
    bool isPowerOfFour(int num) {
        if (num <= 0)
            return 0;
        if (num == 1)
            return true;
        return 2147483648 % num == 0 && (num % 10 == 4 || num % 10 == 6);
    }
};
