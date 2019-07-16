class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int P) {
        sort(tokens.begin(), tokens.end());
        int curr_pts = 0, curr_power = P;
        int i = 0, j = tokens.size() - 1;
        int res = 0;
        while (i <= j) {
            if (curr_power >= tokens[i]) {
                curr_pts++;
                curr_power -= tokens[i];
                i++;
                res = max(res, curr_pts);
            } else if (curr_pts > 0) {
                curr_pts--;
                curr_power += tokens[j];
                j--;
            } else
                break;
        }
        return res;
    }
};
