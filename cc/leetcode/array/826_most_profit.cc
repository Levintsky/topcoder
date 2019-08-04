class Solution {
public:
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        vector<pair<int, int>> jobs;
        for (int i = 0; i < difficulty.size(); ++i) {
            jobs.push_back({profit[i], difficulty[i]});
        }
        sort(jobs.begin(), jobs.end());
        sort(worker.begin(), worker.end());
        
        reverse(jobs.begin(), jobs.end());
        reverse(worker.begin(), worker.end());
        int i = 0, j = 0, res = 0;
        while (i < jobs.size() && j < worker.size()) {
            if (jobs[i].second <= worker[j]) {
                res += jobs[i].first;
                j++;
            } else
                i++;
        }
        return res;
    }
};
