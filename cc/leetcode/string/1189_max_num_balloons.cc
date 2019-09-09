class Solution {
public:
    int maxNumberOfBalloons(string text) {
        string tgt = "balloon";
        vector<int> memo_tgt(26, 0), memo_text(26, 0);
        text_stat(tgt, memo_tgt);
        text_stat(text, memo_text);
        
        int res = -1;
        for (int i = 0; i < 26; ++i) {
            if (memo_tgt[i] > 0) {
                int tmp = memo_text[i] / memo_tgt[i];
                if (res == -1)
                    res = tmp;
                else
                    res = min(res, tmp);
            }
        }
        return res;
    }
    void text_stat(string& text, vector<int>& memo) {
        for (char c : text) {
            memo[c-'a']++;
        }
    }
};
