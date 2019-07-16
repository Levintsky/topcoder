class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> memo;
        int res = 0;
        for (auto item : dominoes) {
            int x = min(item[0], item[1]);
            int y = max(item[0], item[1]);
            res += memo[x*10+y];
            memo[x*10+y]++;
        }
        return res;
    }
};
