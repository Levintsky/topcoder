class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;
        int res1 = nums[0], res2 = 0;
        int tmp;
        for (int i = 1; i < n; ++i) {
            tmp = res1;
            res1 = res2 + nums[i];
            res2 = max(tmp, res2);
        }
        return max(res1, res2);
    }
};