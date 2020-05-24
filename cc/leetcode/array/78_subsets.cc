class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        vector<vector<int>> result;
        vector<int> curr;
        
        backtrack(result, nums, curr, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result,
                   vector<int>& nums,
                   vector<int>& curr,
                   int i) {
        int n = nums.size();
        if (i == n) {
            // vector<int> fin(curr);
            result.push_back(curr);
            return;
        }
        
        // case 1: not including
        backtrack(result, nums, curr, i+1);
        
        // case 2: including
        curr.push_back(nums[i]);
        backtrack(result, nums, curr, i+1);
        curr.pop_back();
    }
};
