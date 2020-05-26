class Solution {
public:
    string orderlyQueue(string S, int K) {
        int n = S.size();
        if (K == 1) { // rotate string
            vector<int> cnt(26);
            char minc = 'z';

            for (char c : S) {
                cnt[c-'a']++;
                minc = min(minc, c);
            }

            string result{S};
            for (int i = 0; i < n; ++i) {
                if (S[i] == minc) {
                    result = min(result, S.substr(i, n-i) + S.substr(0, i));
                }
            }
            return result;
        } else {
            sort(S.begin(), S.end());
            return S;
        }
    }
};
