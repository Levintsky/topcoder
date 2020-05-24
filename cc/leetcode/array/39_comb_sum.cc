class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        
        vector<vector<int>> result;
        vector<int> curr;
        backtrack(result, candidates, curr, 0, target);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result,
                   vector<int>& candidates,
                   vector<int> curr,
                   int index,
                   int remain) {
        if (remain < 0)
            return;
        if (remain == 0) {
            vector<int> fin(curr);
            result.push_back(fin);
        }
        int n = candidates.size();
        for (int i = index; i < n; ++i) {
            curr.push_back(candidates[i]);
            backtrack(result, candidates, curr, i, remain-candidates[i]);
            curr.pop_back();
        }
    }
    
};
