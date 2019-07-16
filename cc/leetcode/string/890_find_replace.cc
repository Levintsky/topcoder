class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        int n = pattern.size();
        vector<int> n_p(n, 0);
        vector<int> n_w(n, 0);
        vector<string> result;
        normalize(n_p, pattern);

        for (auto word : words) {
            normalize(n_w, word);
            if (n_w == n_p)
                result.push_back(word);
        }
        return result;
    }

    void normalize(vector<int>& res, string w) {
        unordered_map<char, int> memo;
        int i = 0;
        for (char c : w) {
            if (memo.find(c) == memo.end())
                memo[c] = memo.size();
            res[i] = memo[c];
            i++;
        }
    }
};
