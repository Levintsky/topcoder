class Solution {
public:
    string lastSubstring(string s) {
        if (s == "")
            return "";
        int n = s.size();
        vector<bool> visited(n, false);
        vector<vector<int>> memo(26);
        for (int i = 0; i < n; ++i) {
            int ind = s[i] - 'a';
            memo[ind].push_back(i);
        }
        // max_char
        char maxc = 'a';
        for (int i = 25; i >= 0; --i) {
            if (memo[i].size() > 0) {
                maxc = 'a' + i;
                for (int j = 0; j < memo[i].size(); ++j)
                    visited[memo[i][j]] = true;
                break;
            }
        }
        vector<int> candidates = memo[maxc - 'a'], new_cand;
        unordered_set<int> to_remove;
        int offset = 1;
        while (candidates.size() > 1) {
            new_cand.clear();
            // next char
            char max_char = 0;
            for (int ind : candidates) {
                if (ind + offset < n)
                    max_char = max(max_char, s[ind + offset]);
            }
            for (int ind : candidates) {
                if (ind + offset >= n)
                    continue;
                if (s[ind + offset] == max_char) {
                    if (visited[ind + offset]) {
                        to_remove.insert(ind + offset);
                    }
                    if (to_remove.find(ind) == to_remove.end())
                        new_cand.push_back(ind);
                }
                visited[ind] = true;
            }
            offset++;
            swap(candidates, new_cand);
        }
        int start = candidates[0];
        return s.substr(start, n - start);
    }
};
