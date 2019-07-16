class Solution {
public:
    int minMoves(vector<int>& nums) {
        auto min_ = min_element(nums.begin(), nums.end());
        int res = 0;
        for (auto item : nums)
            res += item - *min_;
        return res;
    }
};
