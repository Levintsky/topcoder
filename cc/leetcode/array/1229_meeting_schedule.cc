class Solution {
public:
    vector<int> minAvailableDuration(vector<vector<int>>& slots1, vector<vector<int>>& slots2, int duration) {
        for (auto& item : slots2)
            slots1.push_back(item);
        
        sort(slots1.begin(), slots1.end());
        int n = slots1.size();
        vector<int> result;
        
        for (int i = 0; i < n-1; ++i) {
            int start = max(slots1[i][0], slots1[i+1][0]);
            int end = min(slots1[i][1], slots1[i+1][1]);
            if (end - start >= duration) {
                result.push_back(start);
                result.push_back(start + duration);
                return result;
            }
        }
        return result;
    }
};
