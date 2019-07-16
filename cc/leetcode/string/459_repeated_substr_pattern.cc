class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        if (s.size() == 0)
            return true;
        string s2 = s + s;
        s2 = s2.substr(1, 2*s.size()-2);
        return s2.find(s) != string::npos;
    }
};
