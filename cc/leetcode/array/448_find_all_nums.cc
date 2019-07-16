class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            if (nums[i] == -1)
                continue;
            int j = nums[i], k;
            while (j != -1) {
                k = nums[j-1];
                nums[j-1] = -1;
                j = k;
            }
        }
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            if (nums[i] != -1)
                res.push_back(i+1);
        }
        return res;
    }
};
