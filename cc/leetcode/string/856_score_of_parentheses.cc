class Solution {
public:
    int scoreOfParentheses(string S) {
        int last_idx = -1;
        int cum = 0;
        int n = S.size();
        vector<string> slist;
        // split
        for (int i = 0; i < n; ++i) {
            if (S[i] == '(')
                cum++;
            else
                cum--;
            if (cum == 0) {
                slist.push_back(S.substr(last_idx+1, i-last_idx));
                last_idx = i;
            }
        }
        if (slist.size() == 1) {
            if (slist[0] == "()")
                return 1;
            else
                return 2 * scoreOfParentheses(S.substr(1, n-2));
        } else {
            int result = 0;
            for (string item : slist)
                result += scoreOfParentheses(item);
            return result;
        }
    }
};
