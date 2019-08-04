class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string S) {
        int curr = 0, cnt = 1;
        for (char c : S) {
            if (curr + widths[c-'a'] <= 100)
                curr += widths[c-'a'];
            else {
                curr = widths[c-'a'];
                cnt++;
            }
        }
        vector<int> result = {cnt, curr};
        return result;
    }
};
