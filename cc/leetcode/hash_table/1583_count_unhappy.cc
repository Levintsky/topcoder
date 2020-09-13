class Solution {
public:
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
        // friend memo
        unordered_map<int, int> memo_f;
        for (auto& item : pairs) {
            memo_f[item[0]] = item[1];
            memo_f[item[1]] = item[0];
        }
        
        // preference memo
        vector<unordered_map<int, int>> memo_pref;
        for (int i = 0; i < n; ++i) {
            unordered_map<int, int> tmp;
            for (int j = 0; j < n-1; j++)
                tmp[preferences[i][j]] = j;
            memo_pref.push_back(tmp);
        }
        
        // brute force
        unordered_set<int> res;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == j)
                    continue;
                if (memo_pref[i][memo_f[i]] > memo_pref[i][j] && memo_pref[j][memo_f[j]] > memo_pref[j][i]) {
                    res.insert(i);
                    res.insert(j);
                }
            }
        }
        return res.size();
    }
};
