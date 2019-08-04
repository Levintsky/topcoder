class Solution {
public:
    vector<int> smallestSufficientTeam(vector<string>& req_skills, vector<vector<string>>& people) {
        int n = req_skills.size();
        int m = people.size();
        unordered_map<string, int> memo;
        int i = 0;
        for (auto item : req_skills)
            memo[item] = i++;
        unordered_map<int, tuple<int, int, int>> dp; // last-bin, len, idx
        dp[0] = {0, 0, -1};
        
        for (i = 0; i < people.size(); ++i) {
            int his_skill = 0;
            // encode people skill as binary
            for (string skill : people[i]) {
                if (memo.find(skill) != memo.end())
                    his_skill |= 1 << memo[skill];
            }
            // add new items
            unordered_map<int, tuple<int, int, int>> dp2;
            for (auto item : dp) {
                int with_him = item.first | his_skill;
                if (with_him == item.first)
                    continue;
                if (dp.find(with_him) == dp.end() || get<1>(dp[with_him]) > get<1>(item.second) + 1) {
                    dp2[with_him] = {item.first, get<1>(item.second)+1, i};
                }
            }
            // update dp
            for (auto item : dp2) {
                dp[item.first] = item.second;
            }
        }
        // arrange result
        vector<int> final_res;
        int tmp = (1 << n) - 1;
        while (tmp > 0) {
            cout << get<0>(dp[tmp]) << " " << get<1>(dp[tmp]) << " " << get<2>(dp[tmp]) << endl;
            final_res.push_back(get<2>(dp[tmp]));
            tmp = get<0>(dp[tmp]);
        }
        return final_res;
    }
};