class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        static int fast_io = []() { std::ios::sync_with_stdio(false); cin.tie(nullptr);
                                    return 0; }();
        vector<int> res(2);
        auto begin = lower_bound(nums.begin(), nums.end(), target);
        if (begin == nums.end() || *begin != target) {
            res[0] = -1;
            res[1] = -1;
            return res;
        }
        auto end = upper_bound(nums.begin(), nums.end(), target);
        res[0] = begin - nums.begin();
        res[1] = end - nums.begin() - 1;
        return res;
    }
};
