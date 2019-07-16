class Solution {
public:
    int countSegments(string s) {
        int n = s.size();
        if (n == 0)
            return 0;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] != ' ' && i == n-1)
                res++;
            else if (i < n-1 && s[i] != ' ' && s[i+1] == ' ')
                res++;
        }
        return res;
    }
};
