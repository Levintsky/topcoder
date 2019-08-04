class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        vector<int> memo1(256, 0);
        vector<int> memo2(256, 0);
        cnt(chars, memo1);
        
        int res = 0;
        for (string& w : words) {
            cnt(w, memo2);
            bool flag = true;
            for (int i = 0; i < 256; ++i) {
                if (memo1[i] < memo2[i]) {
                    flag = false;
                    break;
                }
            }
            if (flag)
                res += w.size();
        }
        return res;
    }
    
    void cnt(string& w, vector<int>& arr) {
        fill(arr.begin(), arr.end(), 0);
        for (char c : w) {
            arr[c] += 1;
        }
    }
};
