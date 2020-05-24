class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        map<int, int> m;
        // vector<int> curr;
        vector<vector<int>> result{{}};
        for (int item : nums)
            m[item]++;
        
        // iterative
        for (auto item : m) {
            int n = result.size();
            for (int i = 0; i < n; ++i) {
                vector<int> tmp(result[i]);
                // append 0 to item.second item.first
                
                for (int j = 1; j <= item.second; ++j) {
                    tmp.push_back(item.first);
                    result.push_back(tmp);
                }
            }
        }
        
        return result;
    }
    
};
