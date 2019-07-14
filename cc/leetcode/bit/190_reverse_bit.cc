class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t base = 0;
        for (int i = 0; i < 32; ++i) {
            base += (n % 2) * pow(2, 31-i);
            n /= 2;
        }
        return base;
    }
};