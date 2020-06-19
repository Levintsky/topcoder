class Solution {
public:
    bool canDivideIntoSubsequences(vector<int>& nums, int K) {
        int rec = 0;
        int i = 0, n = nums.size();
        for (int j = 0; j < n; ++j) {
            if (nums[j] == nums[i])
                rec = max(rec, j-i+1);
            else
                i = j;
        }
        return rec * K <= nums.size();       
    }
};
