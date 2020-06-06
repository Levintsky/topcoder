class Solution {
public:
    static bool compare(const string& a, const string& b) {
        return a.size() < b.size();
    }
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), compare);
        unordered_map<string, int> dp;
        
        int res = 0;
        for (string item : words) {
            for (int i = 0; i < item.size(); ++i) {
                string item2 = item.substr(0, i) + item.substr(i+1);
                dp[item] = max(dp[item], dp[item2]+1);
                res = max(res, dp[item]);
            }
        }
        return res;
    }
};
