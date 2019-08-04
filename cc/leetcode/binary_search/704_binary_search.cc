class Solution {
public:
    int search(vector<int>& nums, int target) {
        static int fast_io = []() { std::ios::sync_with_stdio(false); cin.tie(nullptr); 
                                    return 0; }();
        auto res = lower_bound(nums.begin(), nums.end(), target);
        if (res != nums.end() && *res == target)
            return res - nums.begin();
        else
            return -1;
    }
};
