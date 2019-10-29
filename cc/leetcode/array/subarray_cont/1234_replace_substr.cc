class Solution {
public:
    void helper(int* memo, char c, bool inc=true) {
        int delta = 1;
        if (!inc)
            delta = -1;
        switch (c) {
            case 'Q':
                memo[0] += delta;
                break;
            case 'W':
                memo[1] += delta;
                break;
            case 'E':
                memo[2] += delta;
                break;
            default:
                memo[3] += delta;
        }
    }
    bool check_valid(int* curr, int* memo) {
        for (int i = 0; i < 4; ++i) {
            if (curr[i] < memo[i])
                return false;
        }
        return true;
    }
    
    int balancedString(string s) {
        int nE = s.size() / 4;
        int memo[4] = {0, 0, 0, 0};
        int curr[4] = {0, 0, 0, 0};
        for (char c : s)
            helper(memo, c, true);
        int max_memo = 0;
        for (int i = 0; i < 4; ++i) {
            memo[i] = max(memo[i]-nE, 0);
            max_memo = max(memo[i], max_memo);
        }
        if (max_memo == 0)
            return 0;
        // find shortest valid
        int result = s.size();
        int i = 0;
        for (int j = 0; j < s.size(); ++j) {
            helper(curr, s[j]);
            if (check_valid(curr, memo)) {
                while (check_valid(curr, memo)) {
                    helper(curr, s[i], false);
                    i++;
                }
                i--;
                helper(curr, s[i]);
                result = min(result, j-i+1);
            }
        }
        return result;
    }
};
