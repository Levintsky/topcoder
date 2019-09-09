class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        vector<vector<int>> memo;
        vector<int> integral(26, 0);
        memo.push_back(integral);
        int n = s.size();
        
        // preprocess integral sum
        for (int i = 0; i < n; ++i) {
            vector<int> tmp(memo.back());
            tmp[s[i]-'a']++;
            memo.push_back(tmp);
        }
        
        // process queries
        vector<bool> result;
        for (auto& q : queries) {
            int l = q[0], r = q[1], k = q[2];
            vector<int> tmp(memo[r+1]);
            for (int i = 0; i < 26; ++i)
                tmp[i] -= memo[l][i];
            // statistics of odd
            int odd = 0;
            for (int item : tmp) {
                if (item % 2 == 1)
                    odd++;
            }
            if (odd <= 2 * k + 1)
                result.push_back(true);
            else
                result.push_back(false);
        }
        return result;
    }
};

vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
    int mask = 0;
    vector<int> ps(1);
    for (char c : s)
        ps.emplace_back(mask ^= 1 << (c - 'a'));

    vector<bool> r;
    for (auto &q : queries) {
        int odds = __builtin_popcount(ps[q[1] + 1] ^ ps[q[0]]);
        r.emplace_back(q[2] * 2 >= odds - (q[1] - q[0] + 1) % 2);
    }
    return r;
}
