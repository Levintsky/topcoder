class Solution {
public:
    bool canConvert(string str1, string str2) {
        if (str1 == str2)
            return true;
        int n = str1.size();
        vector<int> memo(26, -1);
        
        for (int i = 0; i < n; ++i) {
            int c1 = str1[i] - 'a', c2 = str2[i] - 'a';
            if (memo[c1] == -1)
                memo[c1] = c2;
            else if (memo[c1] != c2)
                return false;
        }
        
        unordered_set<char> s(str2.begin(), str2.end());
        return s.size() < 26;
    }
};
