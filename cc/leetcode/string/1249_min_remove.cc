class Solution {
public:
    string remove(string& s, char c1, char c2) {
        string result;
        int stat = 0;
        for (char c : s) {
            if (c != c1 && c != c2)
                result += c;
            else if (c == c1) {
                result += c1;
                stat++;
            } else {
                if (stat > 0) {
                    result += c2;
                    stat--;
                }
            }
        }
        return result;
    }
    
    string minRemoveToMakeValid(string s) {
        string tmp = remove(s, '(', ')');
        reverse(tmp.begin(), tmp.end());
        string res = remove(tmp, ')', '(');
        reverse(res.begin(), res.end());
        return res;
    }
};
