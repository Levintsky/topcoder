class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        unordered_map<long, int> memo;
        int n = points.size();
        int res = 0;
        for (int i = 0; i < n; ++i) {
            memo.clear();
            for (int j = 0; j < n; ++j) {
                if (j == i)
                    continue;
                long dist = pow(points[i][0]-points[j][0],2) + pow(points[i][1]-points[j][1],2);
                memo[dist]++;
            }
            for (auto item : memo) {
                res += item.second * (item.second - 1);
            }
        }
        return res;
    }
};
