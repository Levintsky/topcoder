class Solution {
public:
    int longestDecomposition(string text) {
        int n = text.size();
        if (n == 0)
            return 0;
        int cnt = 1;
        while (cnt * 2 <= n) {
            string a = text.substr(0, cnt);
            string b = text.substr(n-cnt, cnt);
            if (a == b)
                break;
            cnt++;
        }
        if (cnt * 2 <= n) {
            string tmp = text.substr(cnt, n - 2 * cnt);
            return 2 + longestDecomposition(tmp);
        } else
            return 1;
    }
};
