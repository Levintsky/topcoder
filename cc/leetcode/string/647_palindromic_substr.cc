class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        int l, r;
        int res = 0;
        for (int i=0; i < n; i++)
            res += helper(s, i, i) + helper(s, i, i+1);
        return res;
    }
    
    int helper(string& s, int l, int r) {
        int n = s.size();
        while (l >= 0 && r < n && s[l] == s[r]) {
            l--;
            r++;
        }
        return (r-l)/2;
    }
};
