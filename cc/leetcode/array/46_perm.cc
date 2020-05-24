class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result,
                   vector<int>& nums,
                   int i) {
        int n = nums.size();
        if (i == n) {
            result.push_back(nums);
            return;
        }
        
        for (int j = i; j < n; ++j) {
            if (j > i)
                swap(nums[i], nums[j]);
            
            backtrack(result, nums, i+1);
            swap(nums[i], nums[j]);
        }
        
    }
};
