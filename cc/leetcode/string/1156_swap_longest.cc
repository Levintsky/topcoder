class Solution {
public:
    int maxRepOpt1(string text) {
        vector<vector<pair<int, int>>> memo(26);
        int i = 0, j, n = text.size();
        // preprocessing
        while (i < n) {
            j = i + 1;
            while (j < n && text[j] == text[i])
                j++;
            int ind = text[i] - 'a';
            memo[ind].push_back({i, j-1});
            i = j;
        }
        int best = 0, begin, end, lbegin, lend, tmplen;
        for (int i = 0; i < 26; ++i) {
            // sweep
            int m = memo[i].size();
            for (j = 0; j < m; ++j) {
                // single
                begin = memo[i][j].first, end = memo[i][j].second;
                tmplen = end - begin + 1;
                if (m > 1)
                    tmplen++;
                best = max(best, tmplen);
                // double
                if (j > 0) {
                    lbegin = memo[i][j-1].first;
                    lend = memo[i][j-1].second;
                    if (lend + 2 == begin) {
                        tmplen = end - begin + 1 + lend - lbegin + 1;
                        if (m > 2)
                            tmplen++;
                        best = max(best, tmplen);
                    }
                }
            }
        }
        return best;
    }
};
