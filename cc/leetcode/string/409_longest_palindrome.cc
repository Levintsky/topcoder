class Solution {
public:
    int longestPalindrome(string s) {
        array<int, 256> cnt;
        fill(cnt.begin(), cnt.end(), 0);
        for (auto c : s) {
            cnt[c]++;
        }
        bool odd = false;
        int res = 0;
        for (auto item : cnt) {
            if (item % 2 == 0)
                res += item;
            else {
                res += item - 1;
                odd = true;
            }
        }
        if (odd)
            res++;
        return res;
    }
};
