class Solution {
public:
    vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
        int n = words.size(), m = queries.size();
        vector<int> words_stat(n, 0);
        // pre-processing
        for (int i=0; i < n; ++i)
            words_stat[i] = encode(words[i]);
        sort(words_stat.begin(), words_stat.end());
        
        // query
        vector<int> res(m, 0);
        for (int i=0; i < m; ++i) {
            int tmp = encode(queries[i]);
            // binary search
            res[i] = words_stat.end() - upper_bound(words_stat.begin(), words_stat.end(), tmp);
        }
        return res;
    }
    
    int encode(string& s) {
        vector<int> stat(26, 0);
        for (char c : s) {
            stat[c-'a']++;
        }
        for (int i = 0; i < 26; ++i) {
            if (stat[i] > 0)
                return stat[i];
        }
        return 0;
    }
};
