class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<vector<int>> result;

        if (n == 0)
            return result;

        sort(intervals.begin(), intervals.end());
        result.push_back(intervals[0]);
        
        for (int i = 1; i < n; ++i) {
            int curr_end = result.back()[1];
            if (intervals[i][0] <= curr_end) {
                result.back()[1] = max(result.back()[1], intervals[i][1]);
            } else {
                result.push_back(intervals[i]);
            }
        }
        return result;
    }
};
