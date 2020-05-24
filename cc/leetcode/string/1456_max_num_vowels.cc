class Solution {
public:
    int maxVowels(string s, int k) {
        int n = s.size();
        vector<int> v(n);
        unordered_set<char> magic({'a', 'e', 'i', 'o', 'u'});
        int result = 0;
        
        for (int i = 0; i < n; ++i) {
            if (magic.find(s[i]) != magic.end()) {
                if (i == 0)
                    v[0] = 1;
                else
                    v[i] = v[i-1] + 1;
            } else {
                if (i == 0)
                    v[0] = 0;
                else
                    v[i] = v[i-1];
            }
            if (i < k)
                result = max(result, v[i]);
            else
                result = max(result, v[i] - v[i-k]);
        }
        return result;
    }
};

int vowels[26] = {1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1};
int maxVowels(string s, int k) {
    int max_vow = 0;
    for (auto i = 0, cur_vow = 0; i < s.size(); ++i) {
        cur_vow += vowels[s[i] - 'a'];
        if (i >= k)
            cur_vow -= vowels[s[i - k] - 'a'];
        max_vow = max(max_vow, cur_vow);
    }
    return max_vow;
}
