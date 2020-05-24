class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        backtrack(result, nums, 0, nums.size());
        return result;
    }
    
    void backtrack(vector<vector<int>>& result,
                   vector<int> nums,
                   int i, int j) {
        if (i == j-1) {
            result.push_back(nums);
            return;
        }
        
        //backtrack(result, nums, i+1);

        for (int k = i; k < j; ++k) {
            if (i!=k && nums[i] == nums[k])
                continue;
            swap(nums[i], nums[k]);
            backtrack(result, nums, i+1, j);            
        }
        
    }
};
