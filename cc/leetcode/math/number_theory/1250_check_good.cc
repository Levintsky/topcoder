class Solution {
public:
    int gcd(int i, int j) {
        if (i < j)
            swap(i, j);
        if (i % j == 0)
            return j;
        else
            return gcd(i % j, j);
    }
    bool isGoodArray(vector<int>& nums) {
        int res = nums[0];
        for (int item : nums) {
            res = gcd(item, res);
            if (res == 1)
                return true;
        }
        return false;
    }
};
