class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        int res1 = 0, res2 = 0;
        int n = nums.size();
        int max_ = nums[0];
        for (int item : nums)
            max_ = max(max_, item);
        
        for (int i = 0; i < n; ++i) {
            int left = max_, right = max_;
            if (i != 0)
                left = nums[i-1];
            if (i != n-1)
                right = nums[i+1];
            int dec = max(nums[i] - min(left, right) + 1, 0);
            if (i % 2 == 0)
                res1 += dec;
            else
                res2 += dec;
        }
        return min(res1, res2);
    }
};
